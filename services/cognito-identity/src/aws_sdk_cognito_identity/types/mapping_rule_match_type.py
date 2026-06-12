"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MappingRuleMatchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity.errors import DeserializationError

MappingRuleMatchType: TypeAlias = Literal[
    "Equals",
    "Contains",
    "StartsWith",
    "NotEqual",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equals",
        "Contains",
        "StartsWith",
        "NotEqual",
    )
)


def serialize_aws_json_1_1(value: MappingRuleMatchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MappingRuleMatchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MappingRuleMatchType value: {data!r}")
    return cast(MappingRuleMatchType, data)
