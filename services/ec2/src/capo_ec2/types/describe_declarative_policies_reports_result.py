"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeDeclarativePoliciesReportsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.declarative_policies_report_list
    import capo_ec2.types.string


class DescribeDeclarativePoliciesReportsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    reports: NotRequired[
        "capo_ec2.types.declarative_policies_report_list.DeclarativePoliciesReportList"
    ]
    """<p>The report metadata.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeDeclarativePoliciesReportsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "reports" in value:
        import capo_ec2.types.declarative_policies_report_list

        capo_ec2.types.declarative_policies_report_list.serialize_ec2_query(
            value["reports"], pairs, f"{key_prefix}ReportSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeDeclarativePoliciesReportsResult:
    out: DescribeDeclarativePoliciesReportsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_reports = el.find("reportSet")
    if child_reports is not None:
        import capo_ec2.types.declarative_policies_report_list

        out["reports"] = (
            capo_ec2.types.declarative_policies_report_list.deserialize_ec2_query(
                child_reports
            )
        )
    return out
