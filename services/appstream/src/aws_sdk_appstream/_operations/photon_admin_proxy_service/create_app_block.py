"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlock``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_appstream._auth._signers
import aws_sdk_appstream._auth._sigv4
import aws_sdk_appstream.errors.concurrent_modification_exception
import aws_sdk_appstream.errors.limit_exceeded_exception
import aws_sdk_appstream.errors.operation_not_permitted_exception
import aws_sdk_appstream.errors.resource_already_exists_exception
import aws_sdk_appstream.types.app_block
import aws_sdk_appstream.types.create_app_block_request
import aws_sdk_appstream.types.create_app_block_result
import aws_sdk_appstream.types.packaging_type
import aws_sdk_appstream.types.s3_location
import aws_sdk_appstream.types.script_details
import aws_sdk_appstream.types.tags
from aws_sdk_appstream._protocol.errors import parse_error_metadata_json
from aws_sdk_appstream._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_appstream._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_appstream.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            raise aws_sdk_appstream.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_appstream.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            raise aws_sdk_appstream.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "ResourceAlreadyExistsException":
            raise aws_sdk_appstream.errors.resource_already_exists_exception.ResourceAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult:
    out: aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult = (
        aws_sdk_appstream.types.create_app_block_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult:
    out: aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult = (
        aws_sdk_appstream.types.create_app_block_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_appstream._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_appstream._auth._sigv4.build_sigv4_auth_scheme(
                "appstream", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_appstream._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_appstream.types.create_app_block_request.CreateAppBlockRequest,
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
    headers["X-Amz-Target"] = "PhotonAdminProxyService.CreateAppBlock"
    import aws_sdk_appstream.types.create_app_block_request

    body: bytes | None = json.dumps(
        aws_sdk_appstream.types.create_app_block_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_app_block(
    options: OperationOptions,
    input_: aws_sdk_appstream.types.create_app_block_request.CreateAppBlockRequest,
) -> tuple[
    aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult,
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


async def async_create_app_block(
    options: AsyncOperationOptions,
    input_: aws_sdk_appstream.types.create_app_block_request.CreateAppBlockRequest,
) -> tuple[
    aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult,
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
