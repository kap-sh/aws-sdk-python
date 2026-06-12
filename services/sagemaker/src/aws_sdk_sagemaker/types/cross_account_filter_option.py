"""Generated from Smithy shape ``com.amazonaws.sagemaker#CrossAccountFilterOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CrossAccountFilterOption: TypeAlias = Literal[
    "SameAccount",
    "CrossAccount",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SameAccount",
        "CrossAccount",
    )
)


def serialize_aws_json_1_1(value: CrossAccountFilterOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CrossAccountFilterOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrossAccountFilterOption value: {data!r}")
    return cast(CrossAccountFilterOption, data)
