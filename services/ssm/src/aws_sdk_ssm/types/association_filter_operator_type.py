"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilterOperatorType``."""

from typing import Literal, TypeAlias, cast

AssociationFilterOperatorType: TypeAlias = Literal[
    "EQUAL",
    "LESS_THAN",
    "GREATER_THAN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationFilterOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationFilterOperatorType:
    return cast(AssociationFilterOperatorType, data)
