"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMessage``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_chime_sdk_messaging._auth._signers
import aws_sdk_chime_sdk_messaging._auth._sigv4
from aws_sdk_chime_sdk_messaging._protocol.errors import parse_error_metadata_json
from aws_sdk_chime_sdk_messaging._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_chime_sdk_messaging._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_chime_sdk_messaging.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_request
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_chime_sdk_messaging.errors.bad_request_exception

            raise aws_sdk_chime_sdk_messaging.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_chime_sdk_messaging.errors.forbidden_exception

            raise aws_sdk_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_chime_sdk_messaging.errors.not_found_exception

            raise aws_sdk_chime_sdk_messaging.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ServiceFailureException":
            import aws_sdk_chime_sdk_messaging.errors.service_failure_exception

            raise aws_sdk_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_chime_sdk_messaging.errors.service_unavailable_exception

            raise aws_sdk_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottledClientException":
            import aws_sdk_chime_sdk_messaging.errors.throttled_client_exception

            raise aws_sdk_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException.from_json(
                data
            )
        case "UnauthorizedClientException":
            import aws_sdk_chime_sdk_messaging.errors.unauthorized_client_exception

            raise aws_sdk_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse:
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_response

    out: aws_sdk_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse = aws_sdk_chime_sdk_messaging.types.get_channel_message_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_chime_sdk_messaging._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_chime_sdk_messaging._auth._sigv4.build_sigv4_auth_scheme(
                "chime", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_chime_sdk_messaging._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/channels/{ChannelArn}/messages/{MessageId}"
    url = url.replace("{ChannelArn}", quote(str(input_["channel_arn"]), safe=""))
    url = url.replace("{MessageId}", quote(str(input_["message_id"]), safe=""))
    params: dict[str, str] = {}
    if "sub_channel_id" in input_:
        params["sub-channel-id"] = str(input_["sub_channel_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "chime_bearer" in input_:
        headers["x-amz-chime-bearer"] = str(input_["chime_bearer"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_channel_message(
    options: OperationOptions,
    input_: aws_sdk_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest,
) -> tuple[
    aws_sdk_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_get_channel_message(
    options: AsyncOperationOptions,
    input_: aws_sdk_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest,
) -> tuple[
    aws_sdk_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
