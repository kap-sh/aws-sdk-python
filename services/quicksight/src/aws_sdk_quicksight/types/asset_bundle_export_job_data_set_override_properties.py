"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSetOverrideProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list


class AssetBundleExportJobDataSetOverrideProperties(TypedDict):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The ARN of the specific <code>DataSet</code> resource whose override properties are configured in this structure.</p>"""
    properties: "aws_sdk_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list.AssetBundleExportJobDataSetPropertyToOverrideList"
    """<p>A list of <code>DataSet</code> resource properties to generate variables for in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSetOverrideProperties) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list

    out["Properties"] = (
        aws_sdk_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list.serialize_json(
            value["properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobDataSetOverrideProperties:
    out: AssetBundleExportJobDataSetOverrideProperties = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "AssetBundleExportJobDataSetOverrideProperties.arn required"
        )
    if "Properties" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list

        out["properties"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list.deserialize_json(
                data["Properties"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleExportJobDataSetOverrideProperties.properties required"
        )
    return out
