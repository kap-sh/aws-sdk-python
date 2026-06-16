"""Generated from Smithy shape ``com.amazonaws.notifications#ListNotificationConfigurations``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_notifications._auth._signers
import aws_sdk_notifications._auth._sigv4
from aws_sdk_notifications._protocol.errors import parse_error_metadata_json
from aws_sdk_notifications._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_notifications._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_notifications.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.list_notification_configurations_request
    import aws_sdk_notifications.types.list_notification_configurations_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_notifications.errors.access_denied_exception

            raise aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_notifications.errors.internal_server_exception

            raise aws_sdk_notifications.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_notifications.errors.throttling_exception

            raise aws_sdk_notifications.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_notifications.errors.validation_exception

            raise aws_sdk_notifications.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse:
    import aws_sdk_notifications.types.list_notification_configurations_response

    out: aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse = aws_sdk_notifications.types.list_notification_configurations_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_notifications._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_notifications._auth._sigv4.build_sigv4_auth_scheme(
                "notifications", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_notifications._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/notification-configurations"
    params: dict[str, str] = {}
    if "event_rule_source" in input_:
        params["eventRuleSource"] = str(input_["event_rule_source"])
    if "channel_arn" in input_:
        params["channelArn"] = str(input_["channel_arn"])
    if "status" in input_:
        params["status"] = str(input_["status"])
    if "subtype" in input_:
        params["subtype"] = str(input_["subtype"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_notification_configurations(
    options: OperationOptions,
    input_: aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest,
) -> tuple[
    aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse,
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


async def async_list_notification_configurations(
    options: AsyncOperationOptions,
    input_: aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest,
) -> tuple[
    aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse,
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
