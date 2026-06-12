"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformBranchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.platform_branch_summary

PlatformBranchSummaryList: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.platform_branch_summary.PlatformBranchSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformBranchSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.platform_branch_summary

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.platform_branch_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PlatformBranchSummaryList:
    import aws_sdk_elastic_beanstalk.types.platform_branch_summary

    out: PlatformBranchSummaryList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.platform_branch_summary.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PlatformBranchSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.platform_branch_summary

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.platform_branch_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PlatformBranchSummaryList:
    import aws_sdk_elastic_beanstalk.types.platform_branch_summary

    out: PlatformBranchSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.platform_branch_summary.deserialize_query(
                child
            )
        )
    return out
