"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_summary

OperationSummaryList: TypeAlias = list[
    "aws_sdk_route_53_domains.types.operation_summary.OperationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationSummaryList) -> list:
    import aws_sdk_route_53_domains.types.operation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.operation_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationSummaryList:
    import aws_sdk_route_53_domains.types.operation_summary

    out: OperationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.operation_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
