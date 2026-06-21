"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisTask``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_polly._auth._signers
import aws_sdk_polly._auth._sigv4
import aws_sdk_polly.errors.engine_not_supported_exception
import aws_sdk_polly.errors.invalid_s3_bucket_exception
import aws_sdk_polly.errors.invalid_s3_key_exception
import aws_sdk_polly.errors.invalid_sample_rate_exception
import aws_sdk_polly.errors.invalid_sns_topic_arn_exception
import aws_sdk_polly.errors.invalid_ssml_exception
import aws_sdk_polly.errors.language_not_supported_exception
import aws_sdk_polly.errors.lexicon_not_found_exception
import aws_sdk_polly.errors.marks_not_supported_for_format_exception
import aws_sdk_polly.errors.service_failure_exception
import aws_sdk_polly.errors.ssml_marks_not_supported_for_text_type_exception
import aws_sdk_polly.errors.text_length_exceeded_exception
import aws_sdk_polly.types.engine
import aws_sdk_polly.types.language_code
import aws_sdk_polly.types.lexicon_name_list
import aws_sdk_polly.types.output_format
import aws_sdk_polly.types.speech_mark_type_list
import aws_sdk_polly.types.start_speech_synthesis_task_input
import aws_sdk_polly.types.start_speech_synthesis_task_output
import aws_sdk_polly.types.synthesis_task
import aws_sdk_polly.types.text_type
import aws_sdk_polly.types.voice_id
from aws_sdk_polly._protocol.errors import parse_error_metadata_json
from aws_sdk_polly._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_polly._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_polly.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EngineNotSupportedException":
            raise aws_sdk_polly.errors.engine_not_supported_exception.EngineNotSupportedException.from_json(
                data
            )
        case "InvalidS3BucketException":
            raise aws_sdk_polly.errors.invalid_s3_bucket_exception.InvalidS3BucketException.from_json(
                data
            )
        case "InvalidS3KeyException":
            raise aws_sdk_polly.errors.invalid_s3_key_exception.InvalidS3KeyException.from_json(
                data
            )
        case "InvalidSampleRateException":
            raise aws_sdk_polly.errors.invalid_sample_rate_exception.InvalidSampleRateException.from_json(
                data
            )
        case "InvalidSnsTopicArnException":
            raise aws_sdk_polly.errors.invalid_sns_topic_arn_exception.InvalidSnsTopicArnException.from_json(
                data
            )
        case "InvalidSsmlException":
            raise aws_sdk_polly.errors.invalid_ssml_exception.InvalidSsmlException.from_json(
                data
            )
        case "LanguageNotSupportedException":
            raise aws_sdk_polly.errors.language_not_supported_exception.LanguageNotSupportedException.from_json(
                data
            )
        case "LexiconNotFoundException":
            raise aws_sdk_polly.errors.lexicon_not_found_exception.LexiconNotFoundException.from_json(
                data
            )
        case "MarksNotSupportedForFormatException":
            raise aws_sdk_polly.errors.marks_not_supported_for_format_exception.MarksNotSupportedForFormatException.from_json(
                data
            )
        case "ServiceFailureException":
            raise aws_sdk_polly.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case "SsmlMarksNotSupportedForTextTypeException":
            raise aws_sdk_polly.errors.ssml_marks_not_supported_for_text_type_exception.SsmlMarksNotSupportedForTextTypeException.from_json(
                data
            )
        case "TextLengthExceededException":
            raise aws_sdk_polly.errors.text_length_exceeded_exception.TextLengthExceededException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput:
    out: aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput = aws_sdk_polly.types.start_speech_synthesis_task_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput:
    out: aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput = aws_sdk_polly.types.start_speech_synthesis_task_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_polly._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_polly._auth._sigv4.build_sigv4_auth_scheme(
                "polly", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_polly._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/synthesisTasks"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_polly.types.start_speech_synthesis_task_input

    body: bytes | None = json.dumps(
        aws_sdk_polly.types.start_speech_synthesis_task_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_speech_synthesis_task(
    options: OperationOptions,
    input_: aws_sdk_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput,
) -> tuple[
    aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput,
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


async def async_start_speech_synthesis_task(
    options: AsyncOperationOptions,
    input_: aws_sdk_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput,
) -> tuple[
    aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput,
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
