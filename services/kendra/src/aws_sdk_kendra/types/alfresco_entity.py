"""Generated from Smithy shape ``com.amazonaws.kendra#AlfrescoEntity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

AlfrescoEntity: TypeAlias = Literal[
    "wiki",
    "blog",
    "documentLibrary",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "wiki",
        "blog",
        "documentLibrary",
    )
)


def serialize_aws_json_1_1(value: AlfrescoEntity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlfrescoEntity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlfrescoEntity value: {data!r}")
    return cast(AlfrescoEntity, data)
