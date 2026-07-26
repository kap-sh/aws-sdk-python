"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UrlType``."""

from typing import Literal, TypeAlias, cast

UrlType: TypeAlias = Literal[
    "FLINK_DASHBOARD_URL",
    "ZEPPELIN_UI_URL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UrlType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UrlType:
    return cast(UrlType, data)
