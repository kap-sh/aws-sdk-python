"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateApplication``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_appintegrations._auth._signers
import aws_sdk_appintegrations._auth._sigv4
import aws_sdk_appintegrations.errors.access_denied_exception
import aws_sdk_appintegrations.errors.internal_service_error
import aws_sdk_appintegrations.errors.invalid_request_exception
import aws_sdk_appintegrations.errors.resource_not_found_exception
import aws_sdk_appintegrations.errors.throttling_exception
import aws_sdk_appintegrations.errors.unsupported_operation_exception
import aws_sdk_appintegrations.types.application_config
import aws_sdk_appintegrations.types.application_source_config
import aws_sdk_appintegrations.types.application_type
import aws_sdk_appintegrations.types.iframe_config
import aws_sdk_appintegrations.types.permission_list
import aws_sdk_appintegrations.types.publication_list
import aws_sdk_appintegrations.types.subscription_list
import aws_sdk_appintegrations.types.update_application_request
import aws_sdk_appintegrations.types.update_application_response
from aws_sdk_appintegrations._protocol.errors import parse_error_metadata_json
from aws_sdk_appintegrations._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_appintegrations._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_appintegrations.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_appintegrations.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServiceError":
            raise aws_sdk_appintegrations.errors.internal_service_error.InternalServiceError.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_appintegrations.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_appintegrations.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_appintegrations.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnsupportedOperationException":
            raise aws_sdk_appintegrations.errors.unsupported_operation_exception.UnsupportedOperationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse
):
    out: aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse
):
    out: aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_appintegrations._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_appintegrations._auth._sigv4.build_sigv4_auth_scheme(
                "app-integrations", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_appintegrations._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_appintegrations.types.update_application_request.UpdateApplicationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/applications/{Arn}"
    url = url.replace("{Arn}", quote(str(input_["arn"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_appintegrations.types.update_application_request

    body: bytes | None = json.dumps(
        aws_sdk_appintegrations.types.update_application_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PATCH", headers=headers, body=body, context={"signer": signer}
    )


def update_application(
    options: OperationOptions,
    input_: aws_sdk_appintegrations.types.update_application_request.UpdateApplicationRequest,
) -> tuple[
    aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse,
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


async def async_update_application(
    options: AsyncOperationOptions,
    input_: aws_sdk_appintegrations.types.update_application_request.UpdateApplicationRequest,
) -> tuple[
    aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse,
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
