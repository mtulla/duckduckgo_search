import pytest
import warnings

from duckduckgo_search import AsyncDDGS


@pytest.mark.asyncio
async def test_text():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.text("cat", max_results=30)]
        assert len(results) == 30


@pytest.mark.asyncio
async def test_text_params():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.text("cat", safesearch="off", timelimit="m", max_results=30)]
        assert len(results) == 30


@pytest.mark.asyncio
async def test_text_html():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.text("eagle", backend="html", max_results=30)]
        assert len(results) == 30


@pytest.mark.asyncio
async def test_text_lite():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.text("dog", backend="lite", max_results=30)]
        assert len(results) == 30


@pytest.mark.asyncio
async def test_images():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.images("airplane", max_results=140)]
        assert len(results) == 140


@pytest.mark.asyncio
async def test_videos():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.videos("sea", max_results=40)]
        assert len(results) == 40


@pytest.mark.asyncio
async def test_news():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.news("tesla", max_results=27)]
        assert len(results) == 27


@pytest.mark.asyncio
async def test_maps():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.maps("school", place="London", max_results=30)]
        assert len(results) == 30


@pytest.mark.asyncio
async def test_answers():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.answers("sun")]
        assert len(results) >= 1


@pytest.mark.asyncio
async def test_suggestions():
    async with AsyncDDGS() as ddgs:
        results = [x async for x in ddgs.suggestions("moon")]
        assert len(results) >= 1


@pytest.mark.asyncio
async def test_translate():
    results = await AsyncDDGS().translate("school", to="de")
    assert results == {
        "detected_language": "en",
        "translated": "Schule",
        "original": "school",
    }


def test_verify_warning():
    with pytest.warns(UserWarning, match="verify"):
        AsyncDDGS(verify=False)


def test_no_verify_warning():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        AsyncDDGS()


@pytest.mark.asyncio
async def test_verify_false_text():
    async with AsyncDDGS(verify=False) as ddgs:
        results = [x async for x in ddgs.text("cat", max_results=30)]
        assert len(results) == 30