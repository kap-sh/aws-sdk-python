"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationStatusName``."""

from typing import Literal, TypeAlias, cast

AssociationStatusName: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationStatusName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationStatusName:
    return cast(AssociationStatusName, data)
