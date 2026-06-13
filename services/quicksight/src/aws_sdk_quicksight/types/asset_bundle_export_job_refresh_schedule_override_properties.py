"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobRefreshScheduleOverrideProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override_list


class AssetBundleExportJobRefreshScheduleOverrideProperties(TypedDict):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The ARN of the specific <code>RefreshSchedule</code> resource whose override properties are configured in this structure.</p>"""
    properties: "aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override_list.AssetBundleExportJobRefreshSchedulePropertyToOverrideList"
    """<p>A list of <code>RefreshSchedule</code> resource properties to generate variables for in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleExportJobRefreshScheduleOverrideProperties,
) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override_list

    out["Properties"] = (
        aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override_list.serialize_json(
            value["properties"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> AssetBundleExportJobRefreshScheduleOverrideProperties:
    out: AssetBundleExportJobRefreshScheduleOverrideProperties = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "AssetBundleExportJobRefreshScheduleOverrideProperties.arn required"
        )
    if "Properties" in data:
        import aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override_list

        out["properties"] = (
            aws_sdk_quicksight.types.asset_bundle_export_job_refresh_schedule_property_to_override_list.deserialize_json(
                data["Properties"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleExportJobRefreshScheduleOverrideProperties.properties required"
        )
    return out
