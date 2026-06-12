"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HubContentType: TypeAlias = Literal[
    "Model",
    "Notebook",
    "ModelReference",
    "DataSet",
    "JsonDoc",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Model",
        "Notebook",
        "ModelReference",
        "DataSet",
        "JsonDoc",
    )
)


def serialize_aws_json_1_1(value: HubContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubContentType value: {data!r}")
    return cast(HubContentType, data)
