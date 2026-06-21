"""Generated from Smithy shape ``com.amazonaws.sagemaker#SagemakerServicecatalogStatus``."""

from typing import Literal, TypeAlias, cast

SagemakerServicecatalogStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SagemakerServicecatalogStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SagemakerServicecatalogStatus:
    return cast(SagemakerServicecatalogStatus, data)
