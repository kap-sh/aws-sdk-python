"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMountHomeEFS``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMountHomeEFS: TypeAlias = Literal[
    "Enabled",
    "Disabled",
    "DefaultAsDomain",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
        "DefaultAsDomain",
    )
)


def serialize_aws_json_1_1(value: AutoMountHomeEFS) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMountHomeEFS:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMountHomeEFS value: {data!r}")
    return cast(AutoMountHomeEFS, data)
