"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportEntriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_report_entry_list
    import capo_ec2.types.string


class DescribeImageUsageReportEntriesResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    image_usage_report_entries: NotRequired[
        "capo_ec2.types.image_usage_report_entry_list.ImageUsageReportEntryList"
    ]
    """<p>The content of the usage reports.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImageUsageReportEntriesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "image_usage_report_entries" in value:
        import capo_ec2.types.image_usage_report_entry_list

        capo_ec2.types.image_usage_report_entry_list.serialize_ec2_query(
            value["image_usage_report_entries"],
            pairs,
            f"{key_prefix}ImageUsageReportEntrySet",
        )


def deserialize_ec2_query(el: Element) -> DescribeImageUsageReportEntriesResult:
    out: DescribeImageUsageReportEntriesResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_image_usage_report_entries = el.find("imageUsageReportEntrySet")
    if child_image_usage_report_entries is not None:
        import capo_ec2.types.image_usage_report_entry_list

        out["image_usage_report_entries"] = (
            capo_ec2.types.image_usage_report_entry_list.deserialize_ec2_query(
                child_image_usage_report_entries
            )
        )
    return out
