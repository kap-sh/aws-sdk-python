"""Generated from Smithy shape ``com.amazonaws.medialive#ListOfferings``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_medialive._auth._signers
import aws_sdk_medialive._auth._sigv4
from aws_sdk_medialive._protocol.errors import parse_error_metadata_json
from aws_sdk_medialive._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_medialive._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_medialive.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_medialive.types.list_offerings_request
    import aws_sdk_medialive.types.list_offerings_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadGatewayException":
            import aws_sdk_medialive.errors.bad_gateway_exception

            raise aws_sdk_medialive.errors.bad_gateway_exception.BadGatewayException.from_json(
                data
            )
        case "BadRequestException":
            import aws_sdk_medialive.errors.bad_request_exception

            raise aws_sdk_medialive.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_medialive.errors.forbidden_exception

            raise aws_sdk_medialive.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "GatewayTimeoutException":
            import aws_sdk_medialive.errors.gateway_timeout_exception

            raise aws_sdk_medialive.errors.gateway_timeout_exception.GatewayTimeoutException.from_json(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_medialive.errors.internal_server_error_exception

            raise aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_medialive.errors.too_many_requests_exception

            raise aws_sdk_medialive.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_medialive.types.list_offerings_response.ListOfferingsResponse:
    import aws_sdk_medialive.types.list_offerings_response

    out: aws_sdk_medialive.types.list_offerings_response.ListOfferingsResponse = (
        aws_sdk_medialive.types.list_offerings_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_medialive._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_medialive._auth._sigv4.build_sigv4_auth_scheme(
                "medialive", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_medialive._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_medialive.types.list_offerings_request.ListOfferingsRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/prod/offerings"
    params: dict[str, str] = {}
    if "channel_class" in input:
        params["channelClass"] = str(input["channel_class"])
    if "channel_configuration" in input:
        params["channelConfiguration"] = str(input["channel_configuration"])
    if "codec" in input:
        params["codec"] = str(input["codec"])
    if "duration" in input:
        params["duration"] = str(input["duration"])
    if "max_results" in input:
        params["maxResults"] = str(input["max_results"])
    if "maximum_bitrate" in input:
        params["maximumBitrate"] = str(input["maximum_bitrate"])
    if "maximum_framerate" in input:
        params["maximumFramerate"] = str(input["maximum_framerate"])
    if "next_token" in input:
        params["nextToken"] = str(input["next_token"])
    if "resolution" in input:
        params["resolution"] = str(input["resolution"])
    if "resource_type" in input:
        params["resourceType"] = str(input["resource_type"])
    if "special_feature" in input:
        params["specialFeature"] = str(input["special_feature"])
    if "video_quality" in input:
        params["videoQuality"] = str(input["video_quality"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def list_offerings(
    options: OperationOptions,
    input: aws_sdk_medialive.types.list_offerings_request.ListOfferingsRequest,
) -> tuple[
    aws_sdk_medialive.types.list_offerings_response.ListOfferingsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_offerings(
    options: AsyncOperationOptions,
    input: aws_sdk_medialive.types.list_offerings_request.ListOfferingsRequest,
) -> tuple[
    aws_sdk_medialive.types.list_offerings_response.ListOfferingsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
