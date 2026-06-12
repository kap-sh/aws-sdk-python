"""Generated from Smithy shape ``com.amazonaws.codepipeline#TriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

TriggerType: TypeAlias = Literal[
    "CreatePipeline",
    "StartPipelineExecution",
    "PollForSourceChanges",
    "Webhook",
    "CloudWatchEvent",
    "PutActionRevision",
    "WebhookV2",
    "ManualRollback",
    "AutomatedRollback",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreatePipeline",
        "StartPipelineExecution",
        "PollForSourceChanges",
        "Webhook",
        "CloudWatchEvent",
        "PutActionRevision",
        "WebhookV2",
        "ManualRollback",
        "AutomatedRollback",
    )
)


def serialize_aws_json_1_1(value: TriggerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerType value: {data!r}")
    return cast(TriggerType, data)
