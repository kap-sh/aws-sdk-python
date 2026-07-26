"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationType``."""

from typing import Literal, TypeAlias, cast

IntegrationType: TypeAlias = Literal["OPENSEARCH",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntegrationType:
    return cast(IntegrationType, data)
