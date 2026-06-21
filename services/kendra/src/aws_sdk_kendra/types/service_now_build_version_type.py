"""Generated from Smithy shape ``com.amazonaws.kendra#ServiceNowBuildVersionType``."""

from typing import Literal, TypeAlias, cast

ServiceNowBuildVersionType: TypeAlias = Literal[
    "LONDON",
    "OTHERS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceNowBuildVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNowBuildVersionType:
    return cast(ServiceNowBuildVersionType, data)
