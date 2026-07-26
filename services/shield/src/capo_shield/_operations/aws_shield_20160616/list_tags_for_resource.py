"""Generated from Smithy shape ``com.amazonaws.shield#ListTagsForResource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_shield._auth._signers
import capo_shield._auth._sigv4
import capo_shield.errors.internal_error_exception
import capo_shield.errors.invalid_resource_exception
import capo_shield.errors.resource_not_found_exception
import capo_shield.types.list_tags_for_resource_request
import capo_shield.types.list_tags_for_resource_response
import capo_shield.types.tag_list
from capo_shield._protocol.errors import parse_error_metadata_json
from capo_shield._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_shield._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_shield.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalErrorException":
            raise capo_shield.errors.internal_error_exception.InternalErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidResourceException":
            raise capo_shield.errors.invalid_resource_exception.InvalidResourceException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise capo_shield.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse:
    out: capo_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse = capo_shield.types.list_tags_for_resource_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse:
    out: capo_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse = capo_shield.types.list_tags_for_resource_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_shield._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_shield._auth._sigv4.build_sigv4_auth_scheme(
                "shield", options.region
            )
        )
        if sigv4_config is not None:
            return capo_shield._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_shield.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSShield_20160616.ListTagsForResource"
    body: bytes | None = json.dumps(
        capo_shield.types.list_tags_for_resource_request.serialize_aws_json_1_1(input_)
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
    input_: capo_shield.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    capo_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse,
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
    input_: capo_shield.types.list_tags_for_resource_request.ListTagsForResourceRequest,
) -> tuple[
    capo_shield.types.list_tags_for_resource_response.ListTagsForResourceResponse,
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
