"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#GetIceServerConfig``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_kinesis_video_signaling._auth._signers
import capo_kinesis_video_signaling._auth._sigv4
import capo_kinesis_video_signaling.errors.client_limit_exceeded_exception
import capo_kinesis_video_signaling.errors.invalid_argument_exception
import capo_kinesis_video_signaling.errors.invalid_client_exception
import capo_kinesis_video_signaling.errors.not_authorized_exception
import capo_kinesis_video_signaling.errors.resource_not_found_exception
import capo_kinesis_video_signaling.errors.session_expired_exception
import capo_kinesis_video_signaling.types.get_ice_server_config_request
import capo_kinesis_video_signaling.types.get_ice_server_config_response
import capo_kinesis_video_signaling.types.ice_server_list
import capo_kinesis_video_signaling.types.service
from capo_kinesis_video_signaling._protocol.errors import parse_error_metadata_json
from capo_kinesis_video_signaling._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_kinesis_video_signaling._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_kinesis_video_signaling.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ClientLimitExceededException":
            raise capo_kinesis_video_signaling.errors.client_limit_exceeded_exception.ClientLimitExceededException.from_json(
                data
            )
        case "InvalidArgumentException":
            raise capo_kinesis_video_signaling.errors.invalid_argument_exception.InvalidArgumentException.from_json(
                data
            )
        case "InvalidClientException":
            raise capo_kinesis_video_signaling.errors.invalid_client_exception.InvalidClientException.from_json(
                data
            )
        case "NotAuthorizedException":
            raise capo_kinesis_video_signaling.errors.not_authorized_exception.NotAuthorizedException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_kinesis_video_signaling.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "SessionExpiredException":
            raise capo_kinesis_video_signaling.errors.session_expired_exception.SessionExpiredException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse:
    out: capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse = capo_kinesis_video_signaling.types.get_ice_server_config_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse:
    out: capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse = capo_kinesis_video_signaling.types.get_ice_server_config_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_kinesis_video_signaling._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_kinesis_video_signaling._auth._sigv4.build_sigv4_auth_scheme(
                "kinesisvideo", options.region
            )
        )
        if sigv4_config is not None:
            return capo_kinesis_video_signaling._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/get-ice-server-config"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_kinesis_video_signaling.types.get_ice_server_config_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_ice_server_config(
    options: OperationOptions,
    input_: capo_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest,
) -> tuple[
    capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse,
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


async def async_get_ice_server_config(
    options: AsyncOperationOptions,
    input_: capo_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest,
) -> tuple[
    capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse,
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
