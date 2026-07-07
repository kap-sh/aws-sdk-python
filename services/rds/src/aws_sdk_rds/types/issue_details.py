"""Generated from Smithy shape ``com.amazonaws.rds#IssueDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.performance_issue_details


class IssueDetails(TypedDict, closed=True):
    performance_issue_details: NotRequired[
        "aws_sdk_rds.types.performance_issue_details.PerformanceIssueDetails"
    ]
    """<p>A detailed description of the issue when the recommendation category is <code>performance</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IssueDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "performance_issue_details" in value:
        import aws_sdk_rds.types.performance_issue_details

        aws_sdk_rds.types.performance_issue_details.serialize_query(
            value["performance_issue_details"],
            pairs,
            f"{prefix}.PerformanceIssueDetails",
        )


def deserialize_query(el: Element) -> IssueDetails:
    out: IssueDetails = {}  # type: ignore[typeddict-item]
    child_performance_issue_details = el.find("PerformanceIssueDetails")
    if child_performance_issue_details is not None:
        import aws_sdk_rds.types.performance_issue_details

        out["performance_issue_details"] = (
            aws_sdk_rds.types.performance_issue_details.deserialize_query(
                child_performance_issue_details
            )
        )
    return out
