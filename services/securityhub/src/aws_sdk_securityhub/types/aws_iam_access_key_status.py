"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAccessKeyStatus``."""

from typing import Literal, TypeAlias, cast

AwsIamAccessKeyStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAccessKeyStatus) -> str:
    return value


def deserialize_json(data: str) -> AwsIamAccessKeyStatus:
    return cast(AwsIamAccessKeyStatus, data)
