"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemRelatedItemsFilterKey: TypeAlias = Literal[
    "ResourceType",
    "AssociationId",
    "ResourceUri",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceType",
        "AssociationId",
        "ResourceUri",
    )
)


def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemRelatedItemsFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpsItemRelatedItemsFilterKey value: {data!r}"
        )
    return cast(OpsItemRelatedItemsFilterKey, data)
