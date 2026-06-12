"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HttpInstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.http_instance_summary

HttpInstanceSummaryList: TypeAlias = list[
    "aws_sdk_servicediscovery.types.http_instance_summary.HttpInstanceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpInstanceSummaryList) -> list:
    import aws_sdk_servicediscovery.types.http_instance_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_servicediscovery.types.http_instance_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HttpInstanceSummaryList:
    import aws_sdk_servicediscovery.types.http_instance_summary

    out: HttpInstanceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_servicediscovery.types.http_instance_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
