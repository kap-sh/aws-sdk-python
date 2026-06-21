"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchIndexRotationPeriod``."""

from typing import Literal, TypeAlias, cast

ElasticsearchIndexRotationPeriod: TypeAlias = Literal[
    "NoRotation",
    "OneHour",
    "OneDay",
    "OneWeek",
    "OneMonth",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchIndexRotationPeriod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ElasticsearchIndexRotationPeriod:
    return cast(ElasticsearchIndexRotationPeriod, data)
