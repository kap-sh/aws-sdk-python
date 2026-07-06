"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteDashboardsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dashboard_names


class DeleteDashboardsInput(TypedDict, closed=True):
    dashboard_names: NotRequired[
        "aws_sdk_cloudwatch.types.dashboard_names.DashboardNames"
    ]
    """<p>The dashboards to be deleted. This parameter is required.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDashboardsInput) -> dict:
    out: dict = {}
    if "dashboard_names" in value:
        import aws_sdk_cloudwatch.types.dashboard_names

        out["DashboardNames"] = (
            aws_sdk_cloudwatch.types.dashboard_names.serialize_aws_json_1_0(
                value["dashboard_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDashboardsInput:
    out: DeleteDashboardsInput = {}  # type: ignore[typeddict-item]
    if "DashboardNames" in data:
        import aws_sdk_cloudwatch.types.dashboard_names

        out["dashboard_names"] = (
            aws_sdk_cloudwatch.types.dashboard_names.deserialize_aws_json_1_0(
                data["DashboardNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDashboardsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dashboard_names" in value:
        import aws_sdk_cloudwatch.types.dashboard_names

        aws_sdk_cloudwatch.types.dashboard_names.serialize_query(
            value["dashboard_names"], pairs, f"{prefix}.DashboardNames"
        )


def deserialize_query(el: Element) -> DeleteDashboardsInput:
    out: DeleteDashboardsInput = {}  # type: ignore[typeddict-item]
    child_dashboard_names = el.find("DashboardNames")
    if child_dashboard_names is not None:
        import aws_sdk_cloudwatch.types.dashboard_names

        out["dashboard_names"] = (
            aws_sdk_cloudwatch.types.dashboard_names.deserialize_query(
                child_dashboard_names
            )
        )
    return out
