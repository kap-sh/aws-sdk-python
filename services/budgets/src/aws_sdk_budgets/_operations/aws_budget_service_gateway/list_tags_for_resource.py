"""Generated from Smithy shape ``com.amazonaws.budgets#ListTagsForResource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_budgets._auth._signers
import aws_sdk_budgets._auth._sigv4
import aws_sdk_budgets.errors.access_denied_exception
import aws_sdk_budgets.errors.internal_error_exception
import aws_sdk_budgets.errors.invalid_parameter_exception
import aws_sdk_budgets.errors.not_found_exception
import aws_sdk_budgets.errors.throttling_exception
import aws_sdk_budgets.types.list_tags_for_resource_request
import aws_sdk_budgets.types.list_tags_for_resource_response
import aws_sdk_budgets.types.resource_tag_list
from aws_sdk_budgets._protocol.errors import parse_error_metadata_json
from aws_sdk_budgets._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_budgets._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_budgets.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_budgets.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InternalErrorException":
            raise aws_sdk_budgets.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_budgets.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            raise aws_sdk_budgets.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_budgets.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse:
    out: aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse = aws_sdk_budgets.types.list_tags_for_resource_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse:
    out: aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse = aws_sdk_budgets.types.list_tags_for_resource_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_budgets._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_budgets._auth._sigv4.build_sigv4_auth_scheme(
                "budgets", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_budgets._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_budgets.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSBudgetServiceGateway.ListTagsForResource"
    body: bytes | None = json.dumps(
        aws_sdk_budgets.types.list_tags_for_resource_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_tags_for_resource(
    options: OperationOptions,
    input_: aws_sdk_budgets.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse,
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


async def async_list_tags_for_resource(
    options: AsyncOperationOptions,
    input_: aws_sdk_budgets.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse,
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
