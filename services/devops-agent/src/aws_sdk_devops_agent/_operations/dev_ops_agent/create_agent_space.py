"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAgentSpace``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_devops_agent._auth._signers
import aws_sdk_devops_agent._auth._sigv4
from aws_sdk_devops_agent._protocol.errors import parse_error_metadata_json
from aws_sdk_devops_agent._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_devops_agent._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_devops_agent.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.create_agent_space_input
    import aws_sdk_devops_agent.types.create_agent_space_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_devops_agent.errors.access_denied_exception

            raise aws_sdk_devops_agent.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_devops_agent.errors.conflict_exception

            raise aws_sdk_devops_agent.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ContentSizeExceededException":
            import aws_sdk_devops_agent.errors.content_size_exceeded_exception

            raise aws_sdk_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_devops_agent.errors.internal_server_exception

            raise aws_sdk_devops_agent.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_devops_agent.errors.invalid_parameter_exception

            raise aws_sdk_devops_agent.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_devops_agent.errors.resource_not_found_exception

            raise aws_sdk_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            import aws_sdk_devops_agent.errors.service_quota_exceeded_exception

            raise aws_sdk_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_devops_agent.errors.throttling_exception

            raise aws_sdk_devops_agent.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_devops_agent.errors.validation_exception

            raise aws_sdk_devops_agent.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput:
    import aws_sdk_devops_agent.types.create_agent_space_output

    out: aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput = (
        aws_sdk_devops_agent.types.create_agent_space_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_devops_agent._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_devops_agent._auth._sigv4.build_sigv4_auth_scheme(
                "aidevops", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_devops_agent._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/v1/agentspaces"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_devops_agent.types.create_agent_space_input

    body: bytes | None = json.dumps(
        aws_sdk_devops_agent.types.create_agent_space_input.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def create_agent_space(
    options: OperationOptions,
    input: aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput,
) -> tuple[
    aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput,
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


async def async_create_agent_space(
    options: AsyncOperationOptions,
    input: aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput,
) -> tuple[
    aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput,
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
