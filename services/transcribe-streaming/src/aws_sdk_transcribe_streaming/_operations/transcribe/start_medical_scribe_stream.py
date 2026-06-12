"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalScribeStream``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_transcribe_streaming._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_request
    import aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_response


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_request.StartMedicalScribeStreamRequest,
) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")


def start_medical_scribe_stream(
    options: OperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_request.StartMedicalScribeStreamRequest,
) -> tuple[
    aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_response.StartMedicalScribeStreamResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_medical_scribe_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_request.StartMedicalScribeStreamRequest,
) -> tuple[
    aws_sdk_transcribe_streaming.types.start_medical_scribe_stream_response.StartMedicalScribeStreamResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
