"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeUtterance``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_lex_runtime_v2._auth._signers
import aws_sdk_lex_runtime_v2._auth._sigv4
import aws_sdk_lex_runtime_v2.errors.access_denied_exception
import aws_sdk_lex_runtime_v2.errors.bad_gateway_exception
import aws_sdk_lex_runtime_v2.errors.conflict_exception
import aws_sdk_lex_runtime_v2.errors.dependency_failed_exception
import aws_sdk_lex_runtime_v2.errors.internal_server_exception
import aws_sdk_lex_runtime_v2.errors.resource_not_found_exception
import aws_sdk_lex_runtime_v2.errors.throttling_exception
import aws_sdk_lex_runtime_v2.errors.validation_exception
import aws_sdk_lex_runtime_v2.types.blob_stream
import aws_sdk_lex_runtime_v2.types.recognize_utterance_request
import aws_sdk_lex_runtime_v2.types.recognize_utterance_response
from aws_sdk_lex_runtime_v2._protocol.errors import parse_error_metadata_json
from aws_sdk_lex_runtime_v2._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_lex_runtime_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_lex_runtime_v2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "BadGatewayException":
            raise aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_lex_runtime_v2.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "DependencyFailedException":
            raise aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_lex_runtime_v2.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_lex_runtime_v2.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_lex_runtime_v2.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse
):
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "x-amz-lex-input-mode" in response.headers:
        out["input_mode"] = str(response.headers["x-amz-lex-input-mode"])
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "x-amz-lex-messages" in response.headers:
        out["messages"] = str(response.headers["x-amz-lex-messages"])
    if "x-amz-lex-interpretations" in response.headers:
        out["interpretations"] = str(response.headers["x-amz-lex-interpretations"])
    if "x-amz-lex-session-state" in response.headers:
        out["session_state"] = str(response.headers["x-amz-lex-session-state"])
    if "x-amz-lex-request-attributes" in response.headers:
        out["request_attributes"] = str(
            response.headers["x-amz-lex-request-attributes"]
        )
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = str(response.headers["x-amz-lex-session-id"])
    if "x-amz-lex-input-transcript" in response.headers:
        out["input_transcript"] = str(response.headers["x-amz-lex-input-transcript"])
    if "x-amz-lex-recognized-bot-member" in response.headers:
        out["recognized_bot_member"] = str(
            response.headers["x-amz-lex-recognized-bot-member"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse
):
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse = {
        "audio_stream": _iter
    }  # type: ignore[reportAssignmentType]
    if "x-amz-lex-input-mode" in response.headers:
        out["input_mode"] = str(response.headers["x-amz-lex-input-mode"])
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "x-amz-lex-messages" in response.headers:
        out["messages"] = str(response.headers["x-amz-lex-messages"])
    if "x-amz-lex-interpretations" in response.headers:
        out["interpretations"] = str(response.headers["x-amz-lex-interpretations"])
    if "x-amz-lex-session-state" in response.headers:
        out["session_state"] = str(response.headers["x-amz-lex-session-state"])
    if "x-amz-lex-request-attributes" in response.headers:
        out["request_attributes"] = str(
            response.headers["x-amz-lex-request-attributes"]
        )
    if "x-amz-lex-session-id" in response.headers:
        out["session_id"] = str(response.headers["x-amz-lex-session-id"])
    if "x-amz-lex-input-transcript" in response.headers:
        out["input_transcript"] = str(response.headers["x-amz-lex-input-transcript"])
    if "x-amz-lex-recognized-bot-member" in response.headers:
        out["recognized_bot_member"] = str(
            response.headers["x-amz-lex-recognized-bot-member"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lex_runtime_v2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lex_runtime_v2._auth._sigv4.build_sigv4_auth_scheme(
                "lex", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lex_runtime_v2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
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
        + "/bots/{botId}/botAliases/{botAliasId}/botLocales/{localeId}/sessions/{sessionId}/utterance"
    )
    url = url.replace("{botId}", quote(str(input_["bot_id"]), safe=""))
    url = url.replace("{botAliasId}", quote(str(input_["bot_alias_id"]), safe=""))
    url = url.replace("{localeId}", quote(str(input_["locale_id"]), safe=""))
    url = url.replace("{sessionId}", quote(str(input_["session_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_state" in input_:
        headers["x-amz-lex-session-state"] = str(input_["session_state"])
    if "request_attributes" in input_:
        headers["x-amz-lex-request-attributes"] = str(input_["request_attributes"])
    if "request_content_type" in input_:
        headers["Content-Type"] = str(input_["request_content_type"])
    if "response_content_type" in input_:
        headers["Response-Content-Type"] = str(input_["response_content_type"])
    body = input_["input_stream"]
    if isinstance(body, aws_sdk_lex_runtime_v2._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def recognize_utterance(
    options: OperationOptions,
    input_: aws_sdk_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
) -> tuple[
    aws_sdk_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse,
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


async def async_recognize_utterance(
    options: AsyncOperationOptions,
    input_: aws_sdk_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest,
) -> tuple[
    aws_sdk_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse,
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
