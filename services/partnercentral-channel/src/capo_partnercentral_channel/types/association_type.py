"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AssociationType``."""

from typing import Literal, TypeAlias, cast

AssociationType: TypeAlias = Literal[
    "DOWNSTREAM_SELLER",
    "END_CUSTOMER",
    "INTERNAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AssociationType:
    return cast(AssociationType, data)
