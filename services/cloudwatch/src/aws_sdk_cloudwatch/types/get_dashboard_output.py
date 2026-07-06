"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetDashboardOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dashboard_arn
    import aws_sdk_cloudwatch.types.dashboard_body
    import aws_sdk_cloudwatch.types.dashboard_name


class GetDashboardOutput(TypedDict, closed=True):
    dashboard_arn: NotRequired["aws_sdk_cloudwatch.types.dashboard_arn.DashboardArn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    dashboard_body: NotRequired["aws_sdk_cloudwatch.types.dashboard_body.DashboardBody"]
    r"""<p>The detailed information about the dashboard, including what widgets are included and their location on the dashboard. For more information about the <code>DashboardBody</code> syntax, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html\">Dashboard Body Structure and Syntax</a>. </p>"""
    dashboard_name: NotRequired["aws_sdk_cloudwatch.types.dashboard_name.DashboardName"]
    """<p>The name of the dashboard.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDashboardOutput) -> dict:
    out: dict = {}
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "dashboard_body" in value:
        out["DashboardBody"] = value["dashboard_body"]
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDashboardOutput:
    out: GetDashboardOutput = {}  # type: ignore[typeddict-item]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "DashboardBody" in data:
        out["dashboard_body"] = data["DashboardBody"]
    if "DashboardName" in data:
        out["dashboard_name"] = data["DashboardName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDashboardOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dashboard_arn" in value:
        pairs.append((f"{prefix}.DashboardArn", str(value["dashboard_arn"])))
    if "dashboard_body" in value:
        pairs.append((f"{prefix}.DashboardBody", str(value["dashboard_body"])))
    if "dashboard_name" in value:
        pairs.append((f"{prefix}.DashboardName", str(value["dashboard_name"])))


def deserialize_query(el: Element) -> GetDashboardOutput:
    out: GetDashboardOutput = {}  # type: ignore[typeddict-item]
    child_dashboard_arn = el.find("DashboardArn")
    if child_dashboard_arn is not None:
        out["dashboard_arn"] = str(child_dashboard_arn.text or "")
    child_dashboard_body = el.find("DashboardBody")
    if child_dashboard_body is not None:
        out["dashboard_body"] = str(child_dashboard_body.text or "")
    child_dashboard_name = el.find("DashboardName")
    if child_dashboard_name is not None:
        out["dashboard_name"] = str(child_dashboard_name.text or "")
    return out
