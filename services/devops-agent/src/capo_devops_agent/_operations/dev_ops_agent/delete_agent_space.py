"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeleteAgentSpace``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_devops_agent._auth._signers
import capo_devops_agent._auth._sigv4
import capo_devops_agent.errors.access_denied_exception
import capo_devops_agent.errors.conflict_exception
import capo_devops_agent.errors.content_size_exceeded_exception
import capo_devops_agent.errors.internal_server_exception
import capo_devops_agent.errors.invalid_parameter_exception
import capo_devops_agent.errors.resource_not_found_exception
import capo_devops_agent.errors.service_quota_exceeded_exception
import capo_devops_agent.errors.throttling_exception
import capo_devops_agent.errors.validation_exception
import capo_devops_agent.types.delete_agent_space_input
import capo_devops_agent.types.delete_agent_space_output
from capo_devops_agent._protocol.errors import parse_error_metadata_json
from capo_devops_agent._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_devops_agent._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_devops_agent.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_devops_agent.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise capo_devops_agent.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ContentSizeExceededException":
            raise capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_devops_agent.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "InvalidParameterException":
            raise capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_devops_agent.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_devops_agent.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput:
    out: capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput:
    out: capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_devops_agent._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_devops_agent._auth._sigv4.build_sigv4_auth_scheme(
                "aidevops", options.region
            )
        )
        if sigv4_config is not None:
            return capo_devops_agent._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/agentspaces/{agentSpaceId}"
    url = url.replace("{agentSpaceId}", quote(str(input_["agent_space_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_agent_space(
    options: OperationOptions,
    input_: capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput,
) -> tuple[
    capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput,
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


async def async_delete_agent_space(
    options: AsyncOperationOptions,
    input_: capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput,
) -> tuple[
    capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput,
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
