"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetRecommendations``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_codeguruprofiler._auth._signers
import aws_sdk_codeguruprofiler._auth._sigv4
import aws_sdk_codeguruprofiler.errors.internal_server_exception
import aws_sdk_codeguruprofiler.errors.resource_not_found_exception
import aws_sdk_codeguruprofiler.errors.throttling_exception
import aws_sdk_codeguruprofiler.errors.validation_exception
import aws_sdk_codeguruprofiler.types.anomalies
import aws_sdk_codeguruprofiler.types.get_recommendations_request
import aws_sdk_codeguruprofiler.types.get_recommendations_response
import aws_sdk_codeguruprofiler.types.recommendations
import aws_sdk_codeguruprofiler.types.timestamp
from aws_sdk_codeguruprofiler._protocol.errors import parse_error_metadata_json
from aws_sdk_codeguruprofiler._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_codeguruprofiler._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codeguruprofiler.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerException":
            raise aws_sdk_codeguruprofiler.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_codeguruprofiler.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_codeguruprofiler.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse:
    out: aws_sdk_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse = aws_sdk_codeguruprofiler.types.get_recommendations_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse:
    out: aws_sdk_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse = aws_sdk_codeguruprofiler.types.get_recommendations_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codeguruprofiler._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codeguruprofiler._auth._sigv4.build_sigv4_auth_scheme(
                "codeguru-profiler", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codeguruprofiler._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codeguruprofiler.types.get_recommendations_request.GetRecommendationsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/internal/profilingGroups/{profilingGroupName}/recommendations"
    )
    url = url.replace(
        "{profilingGroupName}", quote(str(input_["profiling_group_name"]), safe="")
    )
    params: dict[str, str] = {}
    if "start_time" in input_:
        params["startTime"] = str(input_["start_time"])
    if "end_time" in input_:
        params["endTime"] = str(input_["end_time"])
    if "locale" in input_:
        params["locale"] = str(input_["locale"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_recommendations(
    options: OperationOptions,
    input_: aws_sdk_codeguruprofiler.types.get_recommendations_request.GetRecommendationsRequest,
) -> tuple[
    aws_sdk_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_get_recommendations(
    options: AsyncOperationOptions,
    input_: aws_sdk_codeguruprofiler.types.get_recommendations_request.GetRecommendationsRequest,
) -> tuple[
    aws_sdk_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
