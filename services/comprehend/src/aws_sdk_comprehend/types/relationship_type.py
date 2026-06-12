"""Generated from Smithy shape ``com.amazonaws.comprehend#RelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

RelationshipType: TypeAlias = Literal["CHILD",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CHILD",))


def serialize_aws_json_1_1(value: RelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationshipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelationshipType value: {data!r}")
    return cast(RelationshipType, data)
