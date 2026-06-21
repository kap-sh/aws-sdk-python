"""Generated from Smithy shape ``com.amazonaws.iotdataplane#SendDirectMessage``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_iot_data_plane._auth._signers
import aws_sdk_iot_data_plane._auth._sigv4
import aws_sdk_iot_data_plane.errors.forbidden_exception
import aws_sdk_iot_data_plane.errors.gateway_timeout_exception
import aws_sdk_iot_data_plane.errors.internal_failure_exception
import aws_sdk_iot_data_plane.errors.invalid_request_exception
import aws_sdk_iot_data_plane.errors.request_entity_too_large_exception
import aws_sdk_iot_data_plane.errors.resource_not_found_exception
import aws_sdk_iot_data_plane.errors.throttling_exception
import aws_sdk_iot_data_plane.errors.unauthorized_exception
import aws_sdk_iot_data_plane.types.payload
import aws_sdk_iot_data_plane.types.payload_format_indicator
import aws_sdk_iot_data_plane.types.send_direct_message_request
import aws_sdk_iot_data_plane.types.send_direct_message_response
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
        case "ForbiddenException":
            raise aws_sdk_iot_data_plane.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "GatewayTimeoutException":
            raise aws_sdk_iot_data_plane.errors.gateway_timeout_exception.GatewayTimeoutException.from_json(
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
        case "RequestEntityTooLargeException":
            raise aws_sdk_iot_data_plane.errors.request_entity_too_large_exception.RequestEntityTooLargeException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
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
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse
):
    out: aws_sdk_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse = aws_sdk_iot_data_plane.types.send_direct_message_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse
):
    out: aws_sdk_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse = aws_sdk_iot_data_plane.types.send_direct_message_response.deserialize_json(
        json.loads(await response.aread())
    )
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
    input_: aws_sdk_iot_data_plane.types.send_direct_message_request.SendDirectMessageRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/connections/{clientId}/messages"
    url = url.replace("{clientId}", quote(str(input_["client_id"]), safe=""))
    params: dict[str, str] = {}
    if "topic" in input_:
        params["topic"] = str(input_["topic"])
    if "content_type" in input_:
        params["contentType"] = str(input_["content_type"])
    if "response_topic" in input_:
        params["responseTopic"] = str(input_["response_topic"])
    params["confirmation"] = str(input_.get("confirmation", False))
    params["timeout"] = str(input_.get("timeout", 0))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "user_properties" in input_:
        headers["x-amz-mqtt5-user-properties"] = str(input_["user_properties"])
    if "payload_format_indicator" in input_:
        headers["x-amz-mqtt5-payload-format-indicator"] = str(
            input_["payload_format_indicator"]
        )
    if "correlation_data" in input_:
        headers["x-amz-mqtt5-correlation-data"] = str(input_["correlation_data"])
    if "payload" in input_:
        import aws_sdk_iot_data_plane.types.payload

        body: bytes | None = json.dumps(
            aws_sdk_iot_data_plane.types.payload.serialize_json(input_["payload"])
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


def send_direct_message(
    options: OperationOptions,
    input_: aws_sdk_iot_data_plane.types.send_direct_message_request.SendDirectMessageRequest,
) -> tuple[
    aws_sdk_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse,
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


async def async_send_direct_message(
    options: AsyncOperationOptions,
    input_: aws_sdk_iot_data_plane.types.send_direct_message_request.SendDirectMessageRequest,
) -> tuple[
    aws_sdk_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse,
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
