"""Generated from Smithy shape ``com.amazonaws.sagemaker#Relation``."""

from typing import Literal, TypeAlias, cast

Relation: TypeAlias = Literal[
    "EqualTo",
    "GreaterThanOrEqualTo",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Relation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Relation:
    return cast(Relation, data)
