"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name


class AssetBundleImportJobAnalysisOverrideParameters(TypedDict, closed=True):
    analysis_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the analysis that you ant to apply overrides to.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverrideParameters) -> dict:
    out: dict = {}
    out["AnalysisId"] = value["analysis_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobAnalysisOverrideParameters:
    out: AssetBundleImportJobAnalysisOverrideParameters = {}  # type: ignore[typeddict-item]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverrideParameters.analysis_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
