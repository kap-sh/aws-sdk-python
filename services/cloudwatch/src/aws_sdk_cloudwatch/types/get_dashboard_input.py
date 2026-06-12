"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetDashboardInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dashboard_name


class GetDashboardInput(TypedDict):
    dashboard_name: NotRequired["aws_sdk_cloudwatch.types.dashboard_name.DashboardName"]
    """<p>The name of the dashboard to be described.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDashboardInput) -> dict:
    out: dict = {}
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDashboardInput:
    out: GetDashboardInput = {}  # type: ignore[typeddict-item]
    if "DashboardName" in data:
        out["dashboard_name"] = data["DashboardName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDashboardInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dashboard_name" in value:
        pairs.append((f"{prefix}.DashboardName", str(value["dashboard_name"])))


def deserialize_query(el: Element) -> GetDashboardInput:
    out: GetDashboardInput = {}  # type: ignore[typeddict-item]
    child_dashboard_name = el.find("DashboardName")
    if child_dashboard_name is not None:
        out["dashboard_name"] = str(child_dashboard_name.text or "")
    return out
