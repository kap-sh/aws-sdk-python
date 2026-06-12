"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartStreamTranscription``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_transcribe_streaming._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.start_stream_transcription_request
    import aws_sdk_transcribe_streaming.types.start_stream_transcription_response


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_stream_transcription_request.StartStreamTranscriptionRequest,
) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")


def start_stream_transcription(
    options: OperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_stream_transcription_request.StartStreamTranscriptionRequest,
) -> tuple[
    aws_sdk_transcribe_streaming.types.start_stream_transcription_response.StartStreamTranscriptionResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_stream_transcription(
    options: AsyncOperationOptions,
    input: aws_sdk_transcribe_streaming.types.start_stream_transcription_request.StartStreamTranscriptionRequest,
) -> tuple[
    aws_sdk_transcribe_streaming.types.start_stream_transcription_response.StartStreamTranscriptionResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
