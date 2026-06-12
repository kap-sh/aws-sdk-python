"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ContainerMode: TypeAlias = Literal[
    "SingleModel",
    "MultiModel",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SingleModel",
        "MultiModel",
    )
)


def serialize_aws_json_1_1(value: ContainerMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerMode value: {data!r}")
    return cast(ContainerMode, data)
