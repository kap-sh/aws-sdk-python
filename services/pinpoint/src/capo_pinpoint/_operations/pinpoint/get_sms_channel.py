"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSmsChannel``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_pinpoint._auth._signers
import capo_pinpoint._auth._sigv4
import capo_pinpoint.errors.bad_request_exception
import capo_pinpoint.errors.forbidden_exception
import capo_pinpoint.errors.internal_server_error_exception
import capo_pinpoint.errors.method_not_allowed_exception
import capo_pinpoint.errors.not_found_exception
import capo_pinpoint.errors.payload_too_large_exception
import capo_pinpoint.errors.too_many_requests_exception
import capo_pinpoint.types.get_sms_channel_request
import capo_pinpoint.types.get_sms_channel_response
import capo_pinpoint.types.sms_channel_response
from capo_pinpoint._protocol.errors import parse_error_metadata_json
from capo_pinpoint._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_pinpoint._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_pinpoint.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_pinpoint.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise capo_pinpoint.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "MethodNotAllowedException":
            raise capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException.from_json(
                data
            )
        case "NotFoundException":
            raise capo_pinpoint.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "PayloadTooLargeException":
            raise capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse:
    out: capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse = {
        "sms_channel_response": capo_pinpoint.types.sms_channel_response.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse:
    out: capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse = {
        "sms_channel_response": capo_pinpoint.types.sms_channel_response.deserialize_json(
            json.loads(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_pinpoint._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_pinpoint._auth._sigv4.build_sigv4_auth_scheme(
                "mobiletargeting", options.region
            )
        )
        if sigv4_config is not None:
            return capo_pinpoint._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/apps/{ApplicationId}/channels/sms"
    url = url.replace("{ApplicationId}", quote(str(input_["application_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_sms_channel(
    options: OperationOptions,
    input_: capo_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest,
) -> tuple[
    capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse, zapros.Response
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


async def async_get_sms_channel(
    options: AsyncOperationOptions,
    input_: capo_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest,
) -> tuple[
    capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse, zapros.Response
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
