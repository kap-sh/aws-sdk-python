"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MappingRuleMatchType``."""

from typing import Literal, TypeAlias, cast

MappingRuleMatchType: TypeAlias = Literal[
    "Equals",
    "Contains",
    "StartsWith",
    "NotEqual",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingRuleMatchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MappingRuleMatchType:
    return cast(MappingRuleMatchType, data)
