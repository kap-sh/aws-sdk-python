"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#PutAuditEvents``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudtrail_data._auth._signers
import aws_sdk_cloudtrail_data._auth._sigv4
from aws_sdk_cloudtrail_data._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudtrail_data._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_cloudtrail_data._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudtrail_data.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.put_audit_events_request
    import aws_sdk_cloudtrail_data.types.put_audit_events_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ChannelInsufficientPermission":
            import aws_sdk_cloudtrail_data.errors.channel_insufficient_permission

            raise aws_sdk_cloudtrail_data.errors.channel_insufficient_permission.ChannelInsufficientPermission.from_json(
                data
            )
        case "ChannelNotFound":
            import aws_sdk_cloudtrail_data.errors.channel_not_found

            raise aws_sdk_cloudtrail_data.errors.channel_not_found.ChannelNotFound.from_json(
                data
            )
        case "ChannelUnsupportedSchema":
            import aws_sdk_cloudtrail_data.errors.channel_unsupported_schema

            raise aws_sdk_cloudtrail_data.errors.channel_unsupported_schema.ChannelUnsupportedSchema.from_json(
                data
            )
        case "DuplicatedAuditEventId":
            import aws_sdk_cloudtrail_data.errors.duplicated_audit_event_id

            raise aws_sdk_cloudtrail_data.errors.duplicated_audit_event_id.DuplicatedAuditEventId.from_json(
                data
            )
        case "InvalidChannelARN":
            import aws_sdk_cloudtrail_data.errors.invalid_channel_arn

            raise aws_sdk_cloudtrail_data.errors.invalid_channel_arn.InvalidChannelARN.from_json(
                data
            )
        case "UnsupportedOperationException":
            import aws_sdk_cloudtrail_data.errors.unsupported_operation_exception

            raise aws_sdk_cloudtrail_data.errors.unsupported_operation_exception.UnsupportedOperationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudtrail_data.types.put_audit_events_response.PutAuditEventsResponse:
    import aws_sdk_cloudtrail_data.types.put_audit_events_response

    out: aws_sdk_cloudtrail_data.types.put_audit_events_response.PutAuditEventsResponse = aws_sdk_cloudtrail_data.types.put_audit_events_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudtrail_data._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudtrail_data._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail-data", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudtrail_data._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudtrail_data.types.put_audit_events_request.PutAuditEventsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/PutAuditEvents"
    params: dict[str, str] = {}
    if "channel_arn" in input_:
        params["channelArn"] = str(input_["channel_arn"])
    if "external_id" in input_:
        params["externalId"] = str(input_["external_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_cloudtrail_data.types.put_audit_events_request

    body: bytes | None = json.dumps(
        aws_sdk_cloudtrail_data.types.put_audit_events_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_audit_events(
    options: OperationOptions,
    input_: aws_sdk_cloudtrail_data.types.put_audit_events_request.PutAuditEventsRequest,
) -> tuple[
    aws_sdk_cloudtrail_data.types.put_audit_events_response.PutAuditEventsResponse,
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


async def async_put_audit_events(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudtrail_data.types.put_audit_events_request.PutAuditEventsRequest,
) -> tuple[
    aws_sdk_cloudtrail_data.types.put_audit_events_response.PutAuditEventsResponse,
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
