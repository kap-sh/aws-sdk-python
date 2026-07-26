"""Generated from Smithy shape ``com.amazonaws.licensemanager#RenewType``."""

from typing import Literal, TypeAlias, cast

RenewType: TypeAlias = Literal[
    "None",
    "Weekly",
    "Monthly",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewType:
    return cast(RenewType, data)
