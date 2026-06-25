"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSession``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import aws_sdk_connecthealth._auth._signers
import aws_sdk_connecthealth._auth._sigv4
import aws_sdk_connecthealth._iter
import aws_sdk_connecthealth.errors.access_denied_exception
import aws_sdk_connecthealth.errors.internal_server_exception
import aws_sdk_connecthealth.errors.resource_not_found_exception
import aws_sdk_connecthealth.errors.service_quota_exceeded_exception
import aws_sdk_connecthealth.errors.throttling_exception
import aws_sdk_connecthealth.errors.validation_exception
import aws_sdk_connecthealth.types.medical_scribe_input_stream
import aws_sdk_connecthealth.types.medical_scribe_language_code
import aws_sdk_connecthealth.types.medical_scribe_media_encoding
import aws_sdk_connecthealth.types.medical_scribe_output_stream
import aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input
import aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output
from aws_sdk_connecthealth._protocol.errors import parse_error_metadata_json
from aws_sdk_connecthealth._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_connecthealth._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_connecthealth._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_connecthealth.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_connecthealth.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_connecthealth.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_connecthealth.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_connecthealth.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        aws_sdk_connecthealth.types.medical_scribe_output_stream.deserialize_event_json
    )
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput = {
        "response_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-medscribe-session-id" in response.headers:
        out["session_id"] = str(response.headers["x-amzn-medscribe-session-id"])
    if "x-amzn-medscribe-domain-id" in response.headers:
        out["domain_id"] = str(response.headers["x-amzn-medscribe-domain-id"])
    if "x-amzn-medscribe-subscription-id" in response.headers:
        out["subscription_id"] = str(
            response.headers["x-amzn-medscribe-subscription-id"]
        )
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = str(response.headers["x-amzn-request-id"])
    if "x-amzn-medscribe-language-code" in response.headers:
        out["language_code"] = (
            aws_sdk_connecthealth.types.medical_scribe_language_code.deserialize_json(
                response.headers["x-amzn-medscribe-language-code"]
            )
        )
    if "x-amzn-medscribe-sample-rate" in response.headers:
        out["media_sample_rate_hertz"] = int(
            response.headers["x-amzn-medscribe-sample-rate"]
        )
    if "x-amzn-medscribe-media-encoding" in response.headers:
        out["media_encoding"] = (
            aws_sdk_connecthealth.types.medical_scribe_media_encoding.deserialize_json(
                response.headers["x-amzn-medscribe-media-encoding"]
            )
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput:
    _message_decoder = MessageDecoder()
    _union_deser = (
        aws_sdk_connecthealth.types.medical_scribe_output_stream.deserialize_event_json
    )
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput = {
        "response_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "x-amzn-medscribe-session-id" in response.headers:
        out["session_id"] = str(response.headers["x-amzn-medscribe-session-id"])
    if "x-amzn-medscribe-domain-id" in response.headers:
        out["domain_id"] = str(response.headers["x-amzn-medscribe-domain-id"])
    if "x-amzn-medscribe-subscription-id" in response.headers:
        out["subscription_id"] = str(
            response.headers["x-amzn-medscribe-subscription-id"]
        )
    if "x-amzn-request-id" in response.headers:
        out["request_id"] = str(response.headers["x-amzn-request-id"])
    if "x-amzn-medscribe-language-code" in response.headers:
        out["language_code"] = (
            aws_sdk_connecthealth.types.medical_scribe_language_code.deserialize_json(
                response.headers["x-amzn-medscribe-language-code"]
            )
        )
    if "x-amzn-medscribe-sample-rate" in response.headers:
        out["media_sample_rate_hertz"] = int(
            response.headers["x-amzn-medscribe-sample-rate"]
        )
    if "x-amzn-medscribe-media-encoding" in response.headers:
        out["media_encoding"] = (
            aws_sdk_connecthealth.types.medical_scribe_media_encoding.deserialize_json(
                response.headers["x-amzn-medscribe-media-encoding"]
            )
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_connecthealth._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_connecthealth._auth._sigv4.build_sigv4_auth_scheme(
                "health-agent", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_connecthealth._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/medical-scribe-stream/"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_id" in input_:
        headers["x-amzn-medscribe-session-id"] = str(input_["session_id"])
    if "domain_id" in input_:
        headers["x-amzn-medscribe-domain-id"] = str(input_["domain_id"])
    if "subscription_id" in input_:
        headers["x-amzn-medscribe-subscription-id"] = str(input_["subscription_id"])
    if "language_code" in input_:
        headers["x-amzn-medscribe-language-code"] = str(input_["language_code"])
    if "media_sample_rate_hertz" in input_:
        headers["x-amzn-medscribe-sample-rate"] = str(input_["media_sample_rate_hertz"])
    if "media_encoding" in input_:
        headers["x-amzn-medscribe-media-encoding"] = str(input_["media_encoding"])

    body = aws_sdk_connecthealth._iter.map_sync_iterator(
        input_["input_stream"],
        aws_sdk_connecthealth.types.medical_scribe_input_stream.serialize_event_json,
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
    input_: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/medical-scribe-stream/"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "session_id" in input_:
        headers["x-amzn-medscribe-session-id"] = str(input_["session_id"])
    if "domain_id" in input_:
        headers["x-amzn-medscribe-domain-id"] = str(input_["domain_id"])
    if "subscription_id" in input_:
        headers["x-amzn-medscribe-subscription-id"] = str(input_["subscription_id"])
    if "language_code" in input_:
        headers["x-amzn-medscribe-language-code"] = str(input_["language_code"])
    if "media_sample_rate_hertz" in input_:
        headers["x-amzn-medscribe-sample-rate"] = str(input_["media_sample_rate_hertz"])
    if "media_encoding" in input_:
        headers["x-amzn-medscribe-media-encoding"] = str(input_["media_encoding"])

    body = aws_sdk_connecthealth._iter.map_async_iterator(
        input_["input_stream"],
        aws_sdk_connecthealth.types.medical_scribe_input_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_medical_scribe_listening_session(
    options: OperationOptions,
    input_: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> tuple[
    aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput,
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


async def async_start_medical_scribe_listening_session(
    options: AsyncOperationOptions,
    input_: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> tuple[
    aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput,
    zapros.Response,
]:
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
