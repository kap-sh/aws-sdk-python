"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverrideParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name


class AssetBundleImportJobDashboardOverrideParameters(TypedDict):
    dashboard_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dashboard that you want to apply overrides to.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverrideParameters) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDashboardOverrideParameters:
    out: AssetBundleImportJobDashboardOverrideParameters = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobDashboardOverrideParameters.dashboard_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
