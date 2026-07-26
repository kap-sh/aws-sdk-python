"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotAlias``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lex_models_v2._auth._signers
import capo_lex_models_v2._auth._sigv4
import capo_lex_models_v2.errors.conflict_exception
import capo_lex_models_v2.errors.internal_server_exception
import capo_lex_models_v2.errors.precondition_failed_exception
import capo_lex_models_v2.errors.service_quota_exceeded_exception
import capo_lex_models_v2.errors.throttling_exception
import capo_lex_models_v2.errors.validation_exception
import capo_lex_models_v2.types.bot_alias_locale_settings_map
import capo_lex_models_v2.types.bot_alias_status
import capo_lex_models_v2.types.conversation_log_settings
import capo_lex_models_v2.types.create_bot_alias_request
import capo_lex_models_v2.types.create_bot_alias_response
import capo_lex_models_v2.types.sentiment_analysis_settings
import capo_lex_models_v2.types.tag_map
import capo_lex_models_v2.types.timestamp
from capo_lex_models_v2._protocol.errors import parse_error_metadata_json
from capo_lex_models_v2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lex_models_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_lex_models_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            raise capo_lex_models_v2.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_lex_models_v2.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "PreconditionFailedException":
            raise capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_lex_models_v2.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_lex_models_v2.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse:
    out: capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse = (
        capo_lex_models_v2.types.create_bot_alias_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse:
    out: capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse = (
        capo_lex_models_v2.types.create_bot_alias_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lex_models_v2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_lex_models_v2._auth._sigv4.build_sigv4_auth_scheme(
                "lex", options.region
            )
        )
        if sigv4_config is not None:
            return capo_lex_models_v2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lex_models_v2.types.create_bot_alias_request.CreateBotAliasRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/bots/{botId}/botaliases"
    url = url.replace("{botId}", quote(str(input_["bot_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_lex_models_v2.types.create_bot_alias_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def create_bot_alias(
    options: OperationOptions,
    input_: capo_lex_models_v2.types.create_bot_alias_request.CreateBotAliasRequest,
) -> tuple[
    capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse,
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


async def async_create_bot_alias(
    options: AsyncOperationOptions,
    input_: capo_lex_models_v2.types.create_bot_alias_request.CreateBotAliasRequest,
) -> tuple[
    capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse,
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
