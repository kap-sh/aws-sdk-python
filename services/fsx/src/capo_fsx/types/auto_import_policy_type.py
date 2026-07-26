"""Generated from Smithy shape ``com.amazonaws.fsx#AutoImportPolicyType``."""

from typing import Literal, TypeAlias, cast

AutoImportPolicyType: TypeAlias = Literal[
    "NONE",
    "NEW",
    "NEW_CHANGED",
    "NEW_CHANGED_DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoImportPolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoImportPolicyType:
    return cast(AutoImportPolicyType, data)
