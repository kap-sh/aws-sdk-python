"""Generated from Smithy shape ``com.amazonaws.mediatailor#PutPlaybackConfiguration``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_mediatailor._auth._signers
import aws_sdk_mediatailor._auth._sigv4
import aws_sdk_mediatailor.types.__map_of__string
import aws_sdk_mediatailor.types.ad_conditioning_configuration
import aws_sdk_mediatailor.types.ad_decision_server_configuration
import aws_sdk_mediatailor.types.avail_suppression
import aws_sdk_mediatailor.types.bumper
import aws_sdk_mediatailor.types.cdn_configuration
import aws_sdk_mediatailor.types.configuration_aliases_request
import aws_sdk_mediatailor.types.configuration_aliases_response
import aws_sdk_mediatailor.types.dash_configuration
import aws_sdk_mediatailor.types.dash_configuration_for_put
import aws_sdk_mediatailor.types.function_mapping
import aws_sdk_mediatailor.types.hls_configuration
import aws_sdk_mediatailor.types.insertion_mode
import aws_sdk_mediatailor.types.live_pre_roll_configuration
import aws_sdk_mediatailor.types.log_configuration
import aws_sdk_mediatailor.types.manifest_processing_rules
import aws_sdk_mediatailor.types.put_playback_configuration_request
import aws_sdk_mediatailor.types.put_playback_configuration_response
from aws_sdk_mediatailor._protocol.errors import parse_error_metadata_json
from aws_sdk_mediatailor._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_mediatailor._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_mediatailor.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse:
    out: aws_sdk_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse = aws_sdk_mediatailor.types.put_playback_configuration_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse:
    out: aws_sdk_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse = aws_sdk_mediatailor.types.put_playback_configuration_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_mediatailor._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_mediatailor._auth._sigv4.build_sigv4_auth_scheme(
                "mediatailor", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_mediatailor._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/playbackConfiguration"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_mediatailor.types.put_playback_configuration_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_playback_configuration(
    options: OperationOptions,
    input_: aws_sdk_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest,
) -> tuple[
    aws_sdk_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse,
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


async def async_put_playback_configuration(
    options: AsyncOperationOptions,
    input_: aws_sdk_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest,
) -> tuple[
    aws_sdk_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse,
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
