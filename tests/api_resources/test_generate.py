# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_11 import MeorphisTest11, AsyncMeorphisTest11
from meorphis_test_11.types import Generation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest11) -> None:
        generate = client.generate.create(
            prompt="Please explain to me how LLMs work",
        )
        assert_matches_type(Generation, generate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest11) -> None:
        generate = client.generate.create(
            prompt="Please explain to me how LLMs work",
            end_sequences=["string", "string", "string"],
            frequency_penalty=0,
            k=0,
            logit_bias={"foo": 0},
            max_tokens=0,
            model="string",
            num_generations=0,
            p=0,
            presence_penalty=0,
            preset="my-preset-a58sbd",
            return_likelihoods="GENERATION",
            stop_sequences=["string", "string", "string"],
            stream=True,
            temperature=0,
            truncate="NONE",
        )
        assert_matches_type(Generation, generate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest11) -> None:
        response = client.generate.with_raw_response.create(
            prompt="Please explain to me how LLMs work",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(Generation, generate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest11) -> None:
        with client.generate.with_streaming_response.create(
            prompt="Please explain to me how LLMs work",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(Generation, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest11) -> None:
        generate = await async_client.generate.create(
            prompt="Please explain to me how LLMs work",
        )
        assert_matches_type(Generation, generate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest11) -> None:
        generate = await async_client.generate.create(
            prompt="Please explain to me how LLMs work",
            end_sequences=["string", "string", "string"],
            frequency_penalty=0,
            k=0,
            logit_bias={"foo": 0},
            max_tokens=0,
            model="string",
            num_generations=0,
            p=0,
            presence_penalty=0,
            preset="my-preset-a58sbd",
            return_likelihoods="GENERATION",
            stop_sequences=["string", "string", "string"],
            stream=True,
            temperature=0,
            truncate="NONE",
        )
        assert_matches_type(Generation, generate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        response = await async_client.generate.with_raw_response.create(
            prompt="Please explain to me how LLMs work",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(Generation, generate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest11) -> None:
        async with async_client.generate.with_streaming_response.create(
            prompt="Please explain to me how LLMs work",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(Generation, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
