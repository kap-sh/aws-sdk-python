"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarness``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
import aws_sdk_bedrock_agentcore.errors.access_denied_exception
import aws_sdk_bedrock_agentcore.errors.internal_server_exception
import aws_sdk_bedrock_agentcore.errors.resource_not_found_exception
import aws_sdk_bedrock_agentcore.errors.runtime_client_error
import aws_sdk_bedrock_agentcore.errors.throttling_exception
import aws_sdk_bedrock_agentcore.errors.validation_exception
import aws_sdk_bedrock_agentcore.types.harness_allowed_tools
import aws_sdk_bedrock_agentcore.types.harness_messages
import aws_sdk_bedrock_agentcore.types.harness_model_configuration
import aws_sdk_bedrock_agentcore.types.harness_skills
import aws_sdk_bedrock_agentcore.types.harness_system_prompt
import aws_sdk_bedrock_agentcore.types.harness_tools
import aws_sdk_bedrock_agentcore.types.invoke_harness_request
import aws_sdk_bedrock_agentcore.types.invoke_harness_response
import aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output
from aws_sdk_bedrock_agentcore._protocol.errors import parse_error_metadata_json
from aws_sdk_bedrock_agentcore._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_bedrock_agentcore._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_bedrock_agentcore.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "RuntimeClientError":
            raise aws_sdk_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse = {
        "stream": cast(Any, raw_stream_to_events(_iter, _message_decoder, _union_deser))
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse = {
        "stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_bedrock_agentcore._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_bedrock_agentcore._auth._sigv4.build_sigv4_auth_scheme(
                "bedrock-agentcore", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_bedrock_agentcore._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/harnesses/invoke"
    params: dict[str, str] = {}
    if "harness_arn" in input_:
        params["harnessArn"] = str(input_["harness_arn"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "runtime_session_id" in input_:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"] = str(
            input_["runtime_session_id"]
        )
    if "runtime_user_id" in input_:
        headers["X-Amzn-Bedrock-AgentCore-Runtime-User-Id"] = str(
            input_["runtime_user_id"]
        )
    body: bytes | None = json.dumps(
        aws_sdk_bedrock_agentcore.types.invoke_harness_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_harness(
    options: OperationOptions,
    input_: aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse,
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


async def async_invoke_harness(
    options: AsyncOperationOptions,
    input_: aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse,
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
