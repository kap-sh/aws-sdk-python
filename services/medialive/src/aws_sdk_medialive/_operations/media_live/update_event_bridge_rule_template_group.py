"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateEventBridgeRuleTemplateGroup``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

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
    import aws_sdk_medialive.types.update_event_bridge_rule_template_group_request
    import aws_sdk_medialive.types.update_event_bridge_rule_template_group_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_medialive.errors.bad_request_exception

            raise aws_sdk_medialive.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_medialive.errors.conflict_exception

            raise aws_sdk_medialive.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_medialive.errors.forbidden_exception

            raise aws_sdk_medialive.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_medialive.errors.internal_server_error_exception

            raise aws_sdk_medialive.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_medialive.errors.not_found_exception

            raise aws_sdk_medialive.errors.not_found_exception.NotFoundException.from_json(
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
) -> aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse:
    import aws_sdk_medialive.types.update_event_bridge_rule_template_group_response

    out: aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse = aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.deserialize_json(
        json.loads(response.read())
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
    input: aws_sdk_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = (
        endpoint.url.rstrip("/") + "/prod/eventbridge-rule-template-groups/{Identifier}"
    )
    url = url.replace("{Identifier}", quote(str(input["identifier"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_medialive.types.update_event_bridge_rule_template_group_request

    body: bytes | None = json.dumps(
        aws_sdk_medialive.types.update_event_bridge_rule_template_group_request.serialize_json(
            input
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PATCH",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def update_event_bridge_rule_template_group(
    options: OperationOptions,
    input: aws_sdk_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest,
) -> tuple[
    aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse,
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


async def async_update_event_bridge_rule_template_group(
    options: AsyncOperationOptions,
    input: aws_sdk_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest,
) -> tuple[
    aws_sdk_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse,
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
