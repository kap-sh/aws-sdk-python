"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeFlow``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
import aws_sdk_bedrock_agent_runtime.errors.access_denied_exception
import aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception
import aws_sdk_bedrock_agent_runtime.errors.conflict_exception
import aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception
import aws_sdk_bedrock_agent_runtime.errors.internal_server_exception
import aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception
import aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception
import aws_sdk_bedrock_agent_runtime.errors.throttling_exception
import aws_sdk_bedrock_agent_runtime.errors.validation_exception
import aws_sdk_bedrock_agent_runtime.types.flow_inputs
import aws_sdk_bedrock_agent_runtime.types.flow_response_stream
import aws_sdk_bedrock_agent_runtime.types.invoke_flow_request
import aws_sdk_bedrock_agent_runtime.types.invoke_flow_response
import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration
from aws_sdk_bedrock_agent_runtime._protocol.errors import parse_error_metadata_json
from aws_sdk_bedrock_agent_runtime._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_bedrock_agent_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_bedrock_agent_runtime.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "BadGatewayException":
            raise aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "DependencyFailedException":
            raise aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse:
    _message_decoder = MessageDecoder()
    _union_deser = (
        aws_sdk_bedrock_agent_runtime.types.flow_response_stream.deserialize_event_json
    )
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse = {
        "response_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amz-bedrock-flow-execution-id" in response.headers:
        out["execution_id"] = str(response.headers["x-amz-bedrock-flow-execution-id"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse:
    _message_decoder = MessageDecoder()
    _union_deser = (
        aws_sdk_bedrock_agent_runtime.types.flow_response_stream.deserialize_event_json
    )
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse = {
        "response_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amz-bedrock-flow-execution-id" in response.headers:
        out["execution_id"] = str(response.headers["x-amz-bedrock-flow-execution-id"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_bedrock_agent_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_bedrock_agent_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_bedrock_agent_runtime._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest,
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
        endpoint.url.rstrip("/")
        + "/flows/{flowIdentifier}/aliases/{flowAliasIdentifier}"
    )
    url = url.replace(
        "{flowIdentifier}", quote(str(input_["flow_identifier"]), safe="")
    )
    url = url.replace(
        "{flowAliasIdentifier}", quote(str(input_["flow_alias_identifier"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_flow(
    options: OperationOptions,
    input_: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest,
) -> tuple[
    aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse,
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


async def async_invoke_flow(
    options: AsyncOperationOptions,
    input_: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest,
) -> tuple[
    aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse,
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
