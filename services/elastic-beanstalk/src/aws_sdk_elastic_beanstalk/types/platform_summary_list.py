"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.platform_summary

PlatformSummaryList: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.platform_summary.PlatformSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.platform_summary

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.platform_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PlatformSummaryList:
    import aws_sdk_elastic_beanstalk.types.platform_summary

    out: PlatformSummaryList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.platform_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PlatformSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.platform_summary

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.platform_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PlatformSummaryList:
    import aws_sdk_elastic_beanstalk.types.platform_summary

    out: PlatformSummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.platform_summary.deserialize_query(child)
        )
    return out
