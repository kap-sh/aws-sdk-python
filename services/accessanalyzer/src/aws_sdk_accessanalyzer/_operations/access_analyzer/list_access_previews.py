"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAccessPreviews``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_accessanalyzer._auth._signers
import aws_sdk_accessanalyzer._auth._sigv4
import aws_sdk_accessanalyzer.errors.access_denied_exception
import aws_sdk_accessanalyzer.errors.internal_server_exception
import aws_sdk_accessanalyzer.errors.resource_not_found_exception
import aws_sdk_accessanalyzer.errors.throttling_exception
import aws_sdk_accessanalyzer.errors.validation_exception
import aws_sdk_accessanalyzer.types.access_previews_list
import aws_sdk_accessanalyzer.types.list_access_previews_request
import aws_sdk_accessanalyzer.types.list_access_previews_response
from aws_sdk_accessanalyzer._protocol.errors import parse_error_metadata_json
from aws_sdk_accessanalyzer._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_accessanalyzer._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_accessanalyzer.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_accessanalyzer.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_accessanalyzer.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_accessanalyzer.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_accessanalyzer.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse:
    out: aws_sdk_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse = aws_sdk_accessanalyzer.types.list_access_previews_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse:
    out: aws_sdk_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse = aws_sdk_accessanalyzer.types.list_access_previews_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_accessanalyzer._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_accessanalyzer._auth._sigv4.build_sigv4_auth_scheme(
                "access-analyzer", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_accessanalyzer._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_accessanalyzer.types.list_access_previews_request.ListAccessPreviewsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/access-preview"
    params: dict[str, str] = {}
    if "analyzer_arn" in input_:
        params["analyzerArn"] = str(input_["analyzer_arn"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_access_previews(
    options: OperationOptions,
    input_: aws_sdk_accessanalyzer.types.list_access_previews_request.ListAccessPreviewsRequest,
) -> tuple[
    aws_sdk_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse,
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


async def async_list_access_previews(
    options: AsyncOperationOptions,
    input_: aws_sdk_accessanalyzer.types.list_access_previews_request.ListAccessPreviewsRequest,
) -> tuple[
    aws_sdk_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse,
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
