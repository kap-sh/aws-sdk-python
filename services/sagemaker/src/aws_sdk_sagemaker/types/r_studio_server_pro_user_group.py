"""Generated from Smithy shape ``com.amazonaws.sagemaker#RStudioServerProUserGroup``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RStudioServerProUserGroup: TypeAlias = Literal[
    "R_STUDIO_ADMIN",
    "R_STUDIO_USER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "R_STUDIO_ADMIN",
        "R_STUDIO_USER",
    )
)


def serialize_aws_json_1_1(value: RStudioServerProUserGroup) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RStudioServerProUserGroup:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RStudioServerProUserGroup value: {data!r}")
    return cast(RStudioServerProUserGroup, data)
