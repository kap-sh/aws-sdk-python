"""Generated from Smithy shape ``com.amazonaws.kendra#ServiceNowAuthenticationType``."""

from typing import Literal, TypeAlias, cast

ServiceNowAuthenticationType: TypeAlias = Literal[
    "HTTP_BASIC",
    "OAUTH2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceNowAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNowAuthenticationType:
    return cast(ServiceNowAuthenticationType, data)
