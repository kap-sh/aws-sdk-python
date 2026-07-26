"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppNetworkAccessType``."""

from typing import Literal, TypeAlias, cast

AppNetworkAccessType: TypeAlias = Literal[
    "PublicInternetOnly",
    "VpcOnly",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppNetworkAccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppNetworkAccessType:
    return cast(AppNetworkAccessType, data)
