"""Generated from Smithy shape ``com.amazonaws.route53resolver#Validation``."""

from typing import Literal, TypeAlias, cast

Validation: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Validation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Validation:
    return cast(Validation, data)
