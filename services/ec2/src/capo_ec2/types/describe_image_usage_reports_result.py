"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_report_list
    import capo_ec2.types.string


class DescribeImageUsageReportsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    image_usage_reports: NotRequired[
        "capo_ec2.types.image_usage_report_list.ImageUsageReportList"
    ]
    """<p>The image usage reports.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImageUsageReportsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "image_usage_reports" in value:
        import capo_ec2.types.image_usage_report_list

        capo_ec2.types.image_usage_report_list.serialize_ec2_query(
            value["image_usage_reports"], pairs, f"{key_prefix}ImageUsageReportSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeImageUsageReportsResult:
    out: DescribeImageUsageReportsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_image_usage_reports = el.find("imageUsageReportSet")
    if child_image_usage_reports is not None:
        import capo_ec2.types.image_usage_report_list

        out["image_usage_reports"] = (
            capo_ec2.types.image_usage_report_list.deserialize_ec2_query(
                child_image_usage_reports
            )
        )
    return out
