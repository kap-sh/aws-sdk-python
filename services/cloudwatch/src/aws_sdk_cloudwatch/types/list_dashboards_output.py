"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListDashboardsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dashboard_entries
    import aws_sdk_cloudwatch.types.next_token


class ListDashboardsOutput(TypedDict, closed=True):
    dashboard_entries: NotRequired[
        "aws_sdk_cloudwatch.types.dashboard_entries.DashboardEntries"
    ]
    """<p>The list of matching dashboards.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDashboardsOutput) -> dict:
    out: dict = {}
    if "dashboard_entries" in value:
        import aws_sdk_cloudwatch.types.dashboard_entries

        out["DashboardEntries"] = (
            aws_sdk_cloudwatch.types.dashboard_entries.serialize_aws_json_1_0(
                value["dashboard_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDashboardsOutput:
    out: ListDashboardsOutput = {}  # type: ignore[typeddict-item]
    if "DashboardEntries" in data:
        import aws_sdk_cloudwatch.types.dashboard_entries

        out["dashboard_entries"] = (
            aws_sdk_cloudwatch.types.dashboard_entries.deserialize_aws_json_1_0(
                data["DashboardEntries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListDashboardsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dashboard_entries" in value:
        import aws_sdk_cloudwatch.types.dashboard_entries

        aws_sdk_cloudwatch.types.dashboard_entries.serialize_query(
            value["dashboard_entries"], pairs, f"{prefix}.DashboardEntries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListDashboardsOutput:
    out: ListDashboardsOutput = {}  # type: ignore[typeddict-item]
    child_dashboard_entries = el.find("DashboardEntries")
    if child_dashboard_entries is not None:
        import aws_sdk_cloudwatch.types.dashboard_entries

        out["dashboard_entries"] = (
            aws_sdk_cloudwatch.types.dashboard_entries.deserialize_query(
                child_dashboard_entries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
