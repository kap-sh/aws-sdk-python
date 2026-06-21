"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateImagePermissions``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_appstream._auth._signers
import aws_sdk_appstream._auth._sigv4
import aws_sdk_appstream.errors.limit_exceeded_exception
import aws_sdk_appstream.errors.resource_not_available_exception
import aws_sdk_appstream.errors.resource_not_found_exception
import aws_sdk_appstream.types.image_permissions
import aws_sdk_appstream.types.update_image_permissions_request
import aws_sdk_appstream.types.update_image_permissions_result
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
        case "LimitExceededException":
            raise aws_sdk_appstream.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceNotAvailableException":
            raise aws_sdk_appstream.errors.resource_not_available_exception.ResourceNotAvailableException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_appstream.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult
):
    out: aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult
):
    out: aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult = {}  # type: ignore[typeddict-item]
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
    input_: aws_sdk_appstream.types.update_image_permissions_request.UpdateImagePermissionsRequest,
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
    headers["X-Amz-Target"] = "PhotonAdminProxyService.UpdateImagePermissions"
    import aws_sdk_appstream.types.update_image_permissions_request

    body: bytes | None = json.dumps(
        aws_sdk_appstream.types.update_image_permissions_request.serialize_aws_json_1_1(
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


def update_image_permissions(
    options: OperationOptions,
    input_: aws_sdk_appstream.types.update_image_permissions_request.UpdateImagePermissionsRequest,
) -> tuple[
    aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult,
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


async def async_update_image_permissions(
    options: AsyncOperationOptions,
    input_: aws_sdk_appstream.types.update_image_permissions_request.UpdateImagePermissionsRequest,
) -> tuple[
    aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult,
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
