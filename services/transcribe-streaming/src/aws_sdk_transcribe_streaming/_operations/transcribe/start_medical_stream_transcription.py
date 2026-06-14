"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalStreamTranscription``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_transcribe_streaming._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.start_medical_stream_transcription_request
    import aws_sdk_transcribe_streaming.types.start_medical_stream_transcription_response


def start_medical_stream_transcription(
    options: OperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest,
) -> tuple[
    aws_sdk_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_medical_stream_transcription(
    options: AsyncOperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest,
) -> tuple[
    aws_sdk_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
