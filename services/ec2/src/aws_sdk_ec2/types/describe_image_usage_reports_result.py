"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report_list
    import aws_sdk_ec2.types.string


class DescribeImageUsageReportsResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    image_usage_reports: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_list.ImageUsageReportList"
    ]
    """<p>The image usage reports.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImageUsageReportsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "image_usage_reports" in value:
        import aws_sdk_ec2.types.image_usage_report_list

        aws_sdk_ec2.types.image_usage_report_list.serialize_ec2_query(
            value["image_usage_reports"], pairs, f"{prefix}.ImageUsageReportSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeImageUsageReportsResult:
    out: DescribeImageUsageReportsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ImageUsageReportSet") is not None:
        import aws_sdk_ec2.types.image_usage_report_list

        out["image_usage_reports"] = (
            aws_sdk_ec2.types.image_usage_report_list.deserialize_ec2_query(
                el, "ImageUsageReportSet"
            )
        )
    return out
