"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobThemeOverrideProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override_list


class AssetBundleExportJobThemeOverrideProperties(TypedDict, closed=True):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The ARN of the specific <code>Theme</code> resource whose override properties are configured in this structure.</p>"""
    properties: "aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override_list.AssetBundleExportJobThemePropertyToOverrideList"
    """<p>A list of <code>Theme</code> resource properties to generate variables for in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobThemeOverrideProperties) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override_list

    out["Properties"] = (
        aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override_list.serialize_json(
            value["properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobThemeOverrideProperties:
    out: AssetBundleExportJobThemeOverrideProperties = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "AssetBundleExportJobThemeOverrideProperties.arn required"
        )
    if "Properties" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override_list

        out["properties"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_theme_property_to_override_list.deserialize_json(
                data["Properties"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleExportJobThemeOverrideProperties.properties required"
        )
    return out
