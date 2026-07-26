"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceApiKey``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_grafana._auth._signers
import capo_grafana._auth._sigv4
import capo_grafana.errors.access_denied_exception
import capo_grafana.errors.conflict_exception
import capo_grafana.errors.internal_server_exception
import capo_grafana.errors.resource_not_found_exception
import capo_grafana.errors.service_quota_exceeded_exception
import capo_grafana.errors.throttling_exception
import capo_grafana.errors.validation_exception
import capo_grafana.types.create_workspace_api_key_request
import capo_grafana.types.create_workspace_api_key_response
from capo_grafana._protocol.errors import parse_error_metadata_json
from capo_grafana._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_grafana._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_grafana.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_grafana.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise capo_grafana.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_grafana.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_grafana.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_grafana.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse:
    out: capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse = capo_grafana.types.create_workspace_api_key_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse:
    out: capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse = capo_grafana.types.create_workspace_api_key_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_grafana._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_grafana._auth._sigv4.build_sigv4_auth_scheme(
                "grafana", options.region
            )
        )
        if sigv4_config is not None:
            return capo_grafana._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/workspaces/{workspaceId}/apikeys"
    url = url.replace("{workspaceId}", quote(str(input_["workspace_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_grafana.types.create_workspace_api_key_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_workspace_api_key(
    options: OperationOptions,
    input_: capo_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest,
) -> tuple[
    capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse,
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


async def async_create_workspace_api_key(
    options: AsyncOperationOptions,
    input_: capo_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest,
) -> tuple[
    capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse,
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
