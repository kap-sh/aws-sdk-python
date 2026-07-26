"""Generated from Smithy shape ``com.amazonaws.iot#ReplaceTopicRule``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_iot._auth._signers
import capo_iot._auth._sigv4
import capo_iot.errors.conflicting_resource_update_exception
import capo_iot.errors.internal_exception
import capo_iot.errors.invalid_request_exception
import capo_iot.errors.service_unavailable_exception
import capo_iot.errors.sql_parse_exception
import capo_iot.errors.unauthorized_exception
import capo_iot.types.replace_topic_rule_request
import capo_iot.types.topic_rule_payload
from capo_iot._protocol.errors import parse_error_metadata_json
from capo_iot._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_iot._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_iot.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictingResourceUpdateException":
            raise capo_iot.errors.conflicting_resource_update_exception.ConflictingResourceUpdateException.from_json(
                data
            )
        case "InternalException":
            raise capo_iot.errors.internal_exception.InternalException.from_json(data)
        case "InvalidRequestException":
            raise capo_iot.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_iot.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "SqlParseException":
            raise capo_iot.errors.sql_parse_exception.SqlParseException.from_json(data)
        case "UnauthorizedException":
            raise capo_iot.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_iot._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_iot._auth._sigv4.build_sigv4_auth_scheme("iot", options.region)
        )
        if sigv4_config is not None:
            return capo_iot._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_iot.types.replace_topic_rule_request.ReplaceTopicRuleRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/rules/{ruleName}"
    url = url.replace("{ruleName}", quote(str(input_["rule_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "topic_rule_payload" in input_:
        body: bytes | None = json.dumps(
            capo_iot.types.topic_rule_payload.serialize_json(
                input_["topic_rule_payload"]
            )
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PATCH", headers=headers, body=body, context={"signer": signer}
    )


def replace_topic_rule(
    options: OperationOptions,
    input_: capo_iot.types.replace_topic_rule_request.ReplaceTopicRuleRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_replace_topic_rule(
    options: AsyncOperationOptions,
    input_: capo_iot.types.replace_topic_rule_request.ReplaceTopicRuleRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
