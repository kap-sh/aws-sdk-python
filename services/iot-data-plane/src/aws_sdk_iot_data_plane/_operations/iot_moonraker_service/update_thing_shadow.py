"""Generated from Smithy shape ``com.amazonaws.iotdataplane#UpdateThingShadow``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_iot_data_plane._auth._signers
import aws_sdk_iot_data_plane._auth._sigv4
import aws_sdk_iot_data_plane.errors.conflict_exception
import aws_sdk_iot_data_plane.errors.internal_failure_exception
import aws_sdk_iot_data_plane.errors.invalid_request_exception
import aws_sdk_iot_data_plane.errors.method_not_allowed_exception
import aws_sdk_iot_data_plane.errors.request_entity_too_large_exception
import aws_sdk_iot_data_plane.errors.service_unavailable_exception
import aws_sdk_iot_data_plane.errors.throttling_exception
import aws_sdk_iot_data_plane.errors.unauthorized_exception
import aws_sdk_iot_data_plane.errors.unsupported_document_encoding_exception
import aws_sdk_iot_data_plane.types.json_document
import aws_sdk_iot_data_plane.types.update_thing_shadow_request
import aws_sdk_iot_data_plane.types.update_thing_shadow_response
from aws_sdk_iot_data_plane._protocol.errors import parse_error_metadata_json
from aws_sdk_iot_data_plane._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_iot_data_plane._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_iot_data_plane.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            raise aws_sdk_iot_data_plane.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalFailureException":
            raise aws_sdk_iot_data_plane.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_iot_data_plane.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "MethodNotAllowedException":
            raise aws_sdk_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException.from_json(
                data
            )
        case "RequestEntityTooLargeException":
            raise aws_sdk_iot_data_plane.errors.request_entity_too_large_exception.RequestEntityTooLargeException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_iot_data_plane.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            raise aws_sdk_iot_data_plane.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case "UnsupportedDocumentEncodingException":
            raise aws_sdk_iot_data_plane.errors.unsupported_document_encoding_exception.UnsupportedDocumentEncodingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse
):
    out: aws_sdk_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse = {
        "payload": aws_sdk_iot_data_plane.types.json_document.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse
):
    out: aws_sdk_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse = {
        "payload": aws_sdk_iot_data_plane.types.json_document.deserialize_json(
            json.loads(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iot_data_plane._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iot_data_plane._auth._sigv4.build_sigv4_auth_scheme(
                "iotdata", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_iot_data_plane._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_iot_data_plane.types.update_thing_shadow_request.UpdateThingShadowRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/things/{thingName}/shadow"
    url = url.replace("{thingName}", quote(str(input_["thing_name"]), safe=""))
    params: dict[str, str] = {}
    if "shadow_name" in input_:
        params["name"] = str(input_["shadow_name"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "payload" in input_:
        body: bytes | None = json.dumps(
            aws_sdk_iot_data_plane.types.json_document.serialize_json(input_["payload"])
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_thing_shadow(
    options: OperationOptions,
    input_: aws_sdk_iot_data_plane.types.update_thing_shadow_request.UpdateThingShadowRequest,
) -> tuple[
    aws_sdk_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse,
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


async def async_update_thing_shadow(
    options: AsyncOperationOptions,
    input_: aws_sdk_iot_data_plane.types.update_thing_shadow_request.UpdateThingShadowRequest,
) -> tuple[
    aws_sdk_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse,
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
