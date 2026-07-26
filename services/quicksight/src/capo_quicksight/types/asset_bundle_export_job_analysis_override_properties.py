"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobAnalysisOverrideProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_bundle_export_job_analysis_property_to_override_list


class AssetBundleExportJobAnalysisOverrideProperties(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The ARN of the specific <code>Analysis</code> resource whose override properties are configured in this structure.</p>"""
    properties: "capo_quicksight.types.asset_bundle_export_job_analysis_property_to_override_list.AssetBundleExportJobAnalysisPropertyToOverrideList"
    """<p>A list of <code>Analysis</code> resource properties to generate variables for in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobAnalysisOverrideProperties) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_quicksight.types.asset_bundle_export_job_analysis_property_to_override_list

    out["Properties"] = (
        capo_quicksight.types.asset_bundle_export_job_analysis_property_to_override_list.serialize_json(
            value["properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobAnalysisOverrideProperties:
    out: AssetBundleExportJobAnalysisOverrideProperties = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "AssetBundleExportJobAnalysisOverrideProperties.arn required"
        )
    if "Properties" in data:
        import capo_quicksight.types.asset_bundle_export_job_analysis_property_to_override_list

        out["properties"] = (
            capo_quicksight.types.asset_bundle_export_job_analysis_property_to_override_list.deserialize_json(
                data["Properties"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleExportJobAnalysisOverrideProperties.properties required"
        )
    return out
