"""Generated from Smithy shape ``com.amazonaws.medialive#GetEventBridgeRuleTemplateGroup``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_medialive._auth._signers
import capo_medialive._auth._sigv4
import capo_medialive.errors.bad_request_exception
import capo_medialive.errors.forbidden_exception
import capo_medialive.errors.internal_server_error_exception
import capo_medialive.errors.not_found_exception
import capo_medialive.errors.too_many_requests_exception
import capo_medialive.types.__timestamp_iso8601
import capo_medialive.types.get_event_bridge_rule_template_group_request
import capo_medialive.types.get_event_bridge_rule_template_group_response
import capo_medialive.types.tag_map
from capo_medialive._protocol.errors import parse_error_metadata_json
from capo_medialive._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_medialive._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_medialive.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_medialive.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise capo_medialive.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise capo_medialive.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "NotFoundException":
            raise capo_medialive.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise capo_medialive.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse:
    out: capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse = capo_medialive.types.get_event_bridge_rule_template_group_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse:
    out: capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse = capo_medialive.types.get_event_bridge_rule_template_group_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_medialive._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_medialive._auth._sigv4.build_sigv4_auth_scheme(
                "medialive", options.region
            )
        )
        if sigv4_config is not None:
            return capo_medialive._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/") + "/prod/eventbridge-rule-template-groups/{Identifier}"
    )
    url = url.replace("{Identifier}", quote(str(input_["identifier"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_event_bridge_rule_template_group(
    options: OperationOptions,
    input_: capo_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest,
) -> tuple[
    capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse,
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


async def async_get_event_bridge_rule_template_group(
    options: AsyncOperationOptions,
    input_: capo_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest,
) -> tuple[
    capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse,
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
