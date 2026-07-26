"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#UpdateScope``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_networkflowmonitor._auth._signers
import capo_networkflowmonitor._auth._sigv4
import capo_networkflowmonitor.errors.access_denied_exception
import capo_networkflowmonitor.errors.conflict_exception
import capo_networkflowmonitor.errors.internal_server_exception
import capo_networkflowmonitor.errors.resource_not_found_exception
import capo_networkflowmonitor.errors.service_quota_exceeded_exception
import capo_networkflowmonitor.errors.throttling_exception
import capo_networkflowmonitor.errors.validation_exception
import capo_networkflowmonitor.types.scope_status
import capo_networkflowmonitor.types.tag_map
import capo_networkflowmonitor.types.target_resource_list
import capo_networkflowmonitor.types.update_scope_input
import capo_networkflowmonitor.types.update_scope_output
from capo_networkflowmonitor._protocol.errors import parse_error_metadata_json
from capo_networkflowmonitor._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_networkflowmonitor._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_networkflowmonitor.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise capo_networkflowmonitor.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_networkflowmonitor.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_networkflowmonitor.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_networkflowmonitor.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput:
    out: capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput = (
        capo_networkflowmonitor.types.update_scope_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput:
    out: capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput = (
        capo_networkflowmonitor.types.update_scope_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_networkflowmonitor._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_networkflowmonitor._auth._sigv4.build_sigv4_auth_scheme(
                "networkflowmonitor", options.region
            )
        )
        if sigv4_config is not None:
            return capo_networkflowmonitor._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/scopes/{scopeId}"
    url = url.replace("{scopeId}", quote(str(input_["scope_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_networkflowmonitor.types.update_scope_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PATCH", headers=headers, body=body, context={"signer": signer}
    )


def update_scope(
    options: OperationOptions,
    input_: capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput,
) -> tuple[
    capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput, zapros.Response
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


async def async_update_scope(
    options: AsyncOperationOptions,
    input_: capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput,
) -> tuple[
    capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput, zapros.Response
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
