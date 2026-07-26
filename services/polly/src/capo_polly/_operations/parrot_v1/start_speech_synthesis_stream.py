"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStream``."""

from __future__ import annotations

import json
from typing import Any, cast

import zapros
from typing_extensions import Never

import capo_polly._auth._signers
import capo_polly._auth._sigv4
import capo_polly._iter
import capo_polly.errors.service_failure_exception
import capo_polly.errors.service_quota_exceeded_exception
import capo_polly.errors.throttling_exception
import capo_polly.errors.validation_exception
import capo_polly.types.engine
import capo_polly.types.language_code
import capo_polly.types.lexicon_name_list
import capo_polly.types.output_format
import capo_polly.types.start_speech_synthesis_stream_action_stream
import capo_polly.types.start_speech_synthesis_stream_event_stream
import capo_polly.types.start_speech_synthesis_stream_input
import capo_polly.types.start_speech_synthesis_stream_output
import capo_polly.types.voice_id
from capo_polly._protocol.errors import parse_error_metadata_json
from capo_polly._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from capo_polly._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_polly._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_polly.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ServiceFailureException":
            raise capo_polly.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_polly.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_polly.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_polly.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput:
    _message_decoder = MessageDecoder()
    _union_deser = capo_polly.types.start_speech_synthesis_stream_event_stream.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput = {
        "event_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput:
    _message_decoder = MessageDecoder()
    _union_deser = capo_polly.types.start_speech_synthesis_stream_event_stream.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput = {
        "event_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_polly._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_polly._auth._sigv4.build_sigv4_auth_scheme("polly", options.region)
        )
        if sigv4_config is not None:
            return capo_polly._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/synthesisStream"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "engine" in input_:
        headers["x-amzn-Engine"] = str(input_["engine"])
    if "language_code" in input_:
        headers["x-amzn-LanguageCode"] = str(input_["language_code"])
    if "lexicon_names" in input_:
        headers["x-amzn-LexiconNames"] = str(input_["lexicon_names"])
    if "output_format" in input_:
        headers["x-amzn-OutputFormat"] = str(input_["output_format"])
    if "sample_rate" in input_:
        headers["x-amzn-SampleRate"] = str(input_["sample_rate"])
    if "voice_id" in input_:
        headers["x-amzn-VoiceId"] = str(input_["voice_id"])

    body = capo_polly._iter.map_sync_iterator(
        input_["action_stream"],
        capo_polly.types.start_speech_synthesis_stream_action_stream.serialize_event_json,
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
    input_: capo_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/synthesisStream"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "engine" in input_:
        headers["x-amzn-Engine"] = str(input_["engine"])
    if "language_code" in input_:
        headers["x-amzn-LanguageCode"] = str(input_["language_code"])
    if "lexicon_names" in input_:
        headers["x-amzn-LexiconNames"] = str(input_["lexicon_names"])
    if "output_format" in input_:
        headers["x-amzn-OutputFormat"] = str(input_["output_format"])
    if "sample_rate" in input_:
        headers["x-amzn-SampleRate"] = str(input_["sample_rate"])
    if "voice_id" in input_:
        headers["x-amzn-VoiceId"] = str(input_["voice_id"])

    body = capo_polly._iter.map_async_iterator(
        input_["action_stream"],
        capo_polly.types.start_speech_synthesis_stream_action_stream.serialize_event_json,
    )

    headers["content-type"] = "application/vnd.amazon-eventstream"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_speech_synthesis_stream(
    options: OperationOptions,
    input_: capo_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput,
) -> tuple[
    capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput,
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


async def async_start_speech_synthesis_stream(
    options: AsyncOperationOptions,
    input_: capo_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput,
) -> tuple[
    capo_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput,
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
