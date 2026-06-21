"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#NationalSecurity``."""

from typing import Literal, TypeAlias, cast

NationalSecurity: TypeAlias = Literal[
    "Yes",
    "No",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NationalSecurity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NationalSecurity:
    return cast(NationalSecurity, data)
