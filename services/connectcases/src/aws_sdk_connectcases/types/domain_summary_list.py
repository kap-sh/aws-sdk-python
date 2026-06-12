"""Generated from Smithy shape ``com.amazonaws.connectcases#DomainSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_summary

DomainSummaryList: TypeAlias = list[
    "aws_sdk_connectcases.types.domain_summary.DomainSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummaryList) -> list:
    import aws_sdk_connectcases.types.domain_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.domain_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainSummaryList:
    import aws_sdk_connectcases.types.domain_summary

    out: DomainSummaryList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.domain_summary.deserialize_json(item))
    return out
