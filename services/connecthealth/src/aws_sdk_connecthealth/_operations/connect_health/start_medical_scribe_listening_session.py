"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSession``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_connecthealth._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input
    import aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output


def start_medical_scribe_listening_session(
    options: OperationOptions,
    input: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> tuple[
    aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_medical_scribe_listening_session(
    options: AsyncOperationOptions,
    input: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput,
) -> tuple[
    aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
