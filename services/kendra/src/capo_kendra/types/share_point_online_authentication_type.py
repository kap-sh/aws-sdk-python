"""Generated from Smithy shape ``com.amazonaws.kendra#SharePointOnlineAuthenticationType``."""

from typing import Literal, TypeAlias, cast

SharePointOnlineAuthenticationType: TypeAlias = Literal[
    "HTTP_BASIC",
    "OAUTH2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharePointOnlineAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharePointOnlineAuthenticationType:
    return cast(SharePointOnlineAuthenticationType, data)
