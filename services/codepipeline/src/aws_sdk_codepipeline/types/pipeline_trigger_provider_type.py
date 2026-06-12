"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineTriggerProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

PipelineTriggerProviderType: TypeAlias = Literal["CodeStarSourceConnection",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CodeStarSourceConnection",))


def serialize_aws_json_1_1(value: PipelineTriggerProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineTriggerProviderType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PipelineTriggerProviderType value: {data!r}"
        )
    return cast(PipelineTriggerProviderType, data)
