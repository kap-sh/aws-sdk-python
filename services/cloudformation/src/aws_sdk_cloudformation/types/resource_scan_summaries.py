"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceScanSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_scan_summary

ResourceScanSummaries: TypeAlias = list[
    "aws_sdk_cloudformation.types.resource_scan_summary.ResourceScanSummary"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceScanSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_scan_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_scan_summary.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourceScanSummaries:
    import aws_sdk_cloudformation.types.resource_scan_summary

    out: ResourceScanSummaries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.resource_scan_summary.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ResourceScanSummaries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_scan_summary

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_scan_summary.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourceScanSummaries:
    import aws_sdk_cloudformation.types.resource_scan_summary

    out: ResourceScanSummaries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.resource_scan_summary.deserialize_query(child)
        )
    return out
