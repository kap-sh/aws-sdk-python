"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_summary

DomainSummaryList: TypeAlias = list[
    "aws_sdk_route_53_domains.types.domain_summary.DomainSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSummaryList) -> list:
    import aws_sdk_route_53_domains.types.domain_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.domain_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DomainSummaryList:
    import aws_sdk_route_53_domains.types.domain_summary

    out: DomainSummaryList = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.domain_summary.deserialize_aws_json_1_1(item)
        )
    return out
