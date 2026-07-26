"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteDataRetentionBot``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_wickr._auth._signers
import capo_wickr._auth._sigv4
import capo_wickr.errors.bad_request_error
import capo_wickr.errors.forbidden_error
import capo_wickr.errors.internal_server_error
import capo_wickr.errors.rate_limit_error
import capo_wickr.errors.resource_not_found_error
import capo_wickr.errors.unauthorized_error
import capo_wickr.errors.validation_error
import capo_wickr.types.delete_data_retention_bot_request
import capo_wickr.types.delete_data_retention_bot_response
from capo_wickr._protocol.errors import parse_error_metadata_json
from capo_wickr._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_wickr._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_wickr.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestError":
            raise capo_wickr.errors.bad_request_error.BadRequestError.from_json(data)
        case "ForbiddenError":
            raise capo_wickr.errors.forbidden_error.ForbiddenError.from_json(data)
        case "InternalServerError":
            raise capo_wickr.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "RateLimitError":
            raise capo_wickr.errors.rate_limit_error.RateLimitError.from_json(data)
        case "ResourceNotFoundError":
            raise capo_wickr.errors.resource_not_found_error.ResourceNotFoundError.from_json(
                data
            )
        case "UnauthorizedError":
            raise capo_wickr.errors.unauthorized_error.UnauthorizedError.from_json(data)
        case "ValidationError":
            raise capo_wickr.errors.validation_error.ValidationError.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse:
    out: capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse = capo_wickr.types.delete_data_retention_bot_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse:
    out: capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse = capo_wickr.types.delete_data_retention_bot_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_wickr._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_wickr._auth._sigv4.build_sigv4_auth_scheme("wickr", options.region)
        )
        if sigv4_config is not None:
            return capo_wickr._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_wickr.types.delete_data_retention_bot_request.DeleteDataRetentionBotRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/networks/{networkId}/data-retention-bots"
    url = url.replace("{networkId}", quote(str(input_["network_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_data_retention_bot(
    options: OperationOptions,
    input_: capo_wickr.types.delete_data_retention_bot_request.DeleteDataRetentionBotRequest,
) -> tuple[
    capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse,
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


async def async_delete_data_retention_bot(
    options: AsyncOperationOptions,
    input_: capo_wickr.types.delete_data_retention_bot_request.DeleteDataRetentionBotRequest,
) -> tuple[
    capo_wickr.types.delete_data_retention_bot_response.DeleteDataRetentionBotResponse,
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
