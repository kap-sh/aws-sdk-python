"""Generated from Smithy shape ``com.amazonaws.qbusiness#Chat``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_qbusiness._auth._signers
import aws_sdk_qbusiness._auth._sigv4
import aws_sdk_qbusiness._iter
import aws_sdk_qbusiness.errors.access_denied_exception
import aws_sdk_qbusiness.errors.conflict_exception
import aws_sdk_qbusiness.errors.external_resource_exception
import aws_sdk_qbusiness.errors.internal_server_exception
import aws_sdk_qbusiness.errors.license_not_found_exception
import aws_sdk_qbusiness.errors.resource_not_found_exception
import aws_sdk_qbusiness.errors.throttling_exception
import aws_sdk_qbusiness.errors.validation_exception
import aws_sdk_qbusiness.types.chat_input
import aws_sdk_qbusiness.types.chat_input_stream
import aws_sdk_qbusiness.types.chat_output
import aws_sdk_qbusiness.types.chat_output_stream
import aws_sdk_qbusiness.types.user_groups
from aws_sdk_qbusiness._protocol.errors import parse_error_metadata_json
from aws_sdk_qbusiness._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_qbusiness._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_qbusiness._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_qbusiness.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_qbusiness.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_qbusiness.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ExternalResourceException":
            raise aws_sdk_qbusiness.errors.external_resource_exception.ExternalResourceException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_qbusiness.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "LicenseNotFoundException":
            raise aws_sdk_qbusiness.errors.license_not_found_exception.LicenseNotFoundException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_qbusiness.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_qbusiness.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_qbusiness.types.chat_output.ChatOutput:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_qbusiness.types.chat_output_stream.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_qbusiness.types.chat_output.ChatOutput = {
        "output_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_qbusiness.types.chat_output.ChatOutput:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_qbusiness.types.chat_output_stream.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_qbusiness.types.chat_output.ChatOutput = {
        "output_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_qbusiness._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_qbusiness._auth._sigv4.build_sigv4_auth_scheme(
                "qbusiness", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_qbusiness._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_qbusiness.types.chat_input.ChatInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/applications/{applicationId}/conversations"
    url = url.replace("{applicationId}", quote(str(input_["application_id"]), safe=""))
    params: dict[str, str] = {}
    if "user_id" in input_:
        params["userId"] = str(input_["user_id"])
    if "user_groups" in input_:
        params["userGroups"] = str(input_["user_groups"])
    if "conversation_id" in input_:
        params["conversationId"] = str(input_["conversation_id"])
    if "parent_message_id" in input_:
        params["parentMessageId"] = str(input_["parent_message_id"])
    if "client_token" in input_:
        params["clientToken"] = str(input_["client_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}

    body = aws_sdk_qbusiness._iter.map_sync_iterator(
        input_["input_stream"],
        aws_sdk_qbusiness.types.chat_input_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def async_build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_qbusiness.types.chat_input.ChatInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/applications/{applicationId}/conversations"
    url = url.replace("{applicationId}", quote(str(input_["application_id"]), safe=""))
    params: dict[str, str] = {}
    if "user_id" in input_:
        params["userId"] = str(input_["user_id"])
    if "user_groups" in input_:
        params["userGroups"] = str(input_["user_groups"])
    if "conversation_id" in input_:
        params["conversationId"] = str(input_["conversation_id"])
    if "parent_message_id" in input_:
        params["parentMessageId"] = str(input_["parent_message_id"])
    if "client_token" in input_:
        params["clientToken"] = str(input_["client_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}

    body = aws_sdk_qbusiness._iter.map_async_iterator(
        input_["input_stream"],
        aws_sdk_qbusiness.types.chat_input_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def chat(
    options: OperationOptions, input_: aws_sdk_qbusiness.types.chat_input.ChatInput
) -> tuple[aws_sdk_qbusiness.types.chat_output.ChatOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_chat(
    options: AsyncOperationOptions, input_: aws_sdk_qbusiness.types.chat_input.ChatInput
) -> tuple[aws_sdk_qbusiness.types.chat_output.ChatOutput, zapros.Response]:
    response = await options.client.handler.ahandle(
        async_build_request(options, input_)
    )
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
