"""Generated from Smithy shape ``com.amazonaws.lambda#EventType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

EventType: TypeAlias = Literal[
    "ExecutionStarted",
    "ExecutionSucceeded",
    "ExecutionFailed",
    "ExecutionTimedOut",
    "ExecutionStopped",
    "ContextStarted",
    "ContextSucceeded",
    "ContextFailed",
    "WaitStarted",
    "WaitSucceeded",
    "WaitCancelled",
    "StepStarted",
    "StepSucceeded",
    "StepFailed",
    "ChainedInvokeStarted",
    "ChainedInvokeSucceeded",
    "ChainedInvokeFailed",
    "ChainedInvokeTimedOut",
    "ChainedInvokeStopped",
    "CallbackStarted",
    "CallbackSucceeded",
    "CallbackFailed",
    "CallbackTimedOut",
    "InvocationCompleted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ExecutionStarted",
        "ExecutionSucceeded",
        "ExecutionFailed",
        "ExecutionTimedOut",
        "ExecutionStopped",
        "ContextStarted",
        "ContextSucceeded",
        "ContextFailed",
        "WaitStarted",
        "WaitSucceeded",
        "WaitCancelled",
        "StepStarted",
        "StepSucceeded",
        "StepFailed",
        "ChainedInvokeStarted",
        "ChainedInvokeSucceeded",
        "ChainedInvokeFailed",
        "ChainedInvokeTimedOut",
        "ChainedInvokeStopped",
        "CallbackStarted",
        "CallbackSucceeded",
        "CallbackFailed",
        "CallbackTimedOut",
        "InvocationCompleted",
    )
)


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
