"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanTaskUiStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HumanTaskUiStatus: TypeAlias = Literal[
    "Active",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: HumanTaskUiStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HumanTaskUiStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HumanTaskUiStatus value: {data!r}")
    return cast(HumanTaskUiStatus, data)
