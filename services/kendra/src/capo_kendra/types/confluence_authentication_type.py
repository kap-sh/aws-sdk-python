"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAuthenticationType``."""

from typing import Literal, TypeAlias, cast

ConfluenceAuthenticationType: TypeAlias = Literal[
    "HTTP_BASIC",
    "PAT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceAuthenticationType:
    return cast(ConfluenceAuthenticationType, data)
