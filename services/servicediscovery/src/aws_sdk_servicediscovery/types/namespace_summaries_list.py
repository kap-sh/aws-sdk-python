"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.namespace_summary

NamespaceSummariesList: TypeAlias = list[
    "aws_sdk_servicediscovery.types.namespace_summary.NamespaceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceSummariesList) -> list:
    import aws_sdk_servicediscovery.types.namespace_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_servicediscovery.types.namespace_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NamespaceSummariesList:
    import aws_sdk_servicediscovery.types.namespace_summary

    out: NamespaceSummariesList = []
    for item in data:
        out.append(
            aws_sdk_servicediscovery.types.namespace_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
