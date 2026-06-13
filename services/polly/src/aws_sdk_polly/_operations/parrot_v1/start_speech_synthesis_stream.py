"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStream``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_polly._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_polly.types.start_speech_synthesis_stream_input
    import aws_sdk_polly.types.start_speech_synthesis_stream_output


def start_speech_synthesis_stream(
    options: OperationOptions,
    input: aws_sdk_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput,
) -> tuple[
    aws_sdk_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_speech_synthesis_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput,
) -> tuple[
    aws_sdk_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
