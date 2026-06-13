"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverrideParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_refresh_properties
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_name


class AssetBundleImportJobDataSetOverrideParameters(TypedDict):
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset to apply overrides to.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the dataset.</p>"""
    data_set_refresh_properties: NotRequired[
        "aws_sdk_quicksight.types.data_set_refresh_properties.DataSetRefreshProperties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverrideParameters) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "data_set_refresh_properties" in value:
        import aws_sdk_quicksight.types.data_set_refresh_properties

        out["DataSetRefreshProperties"] = (
            aws_sdk_quicksight.types.data_set_refresh_properties.serialize_json(
                value["data_set_refresh_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSetOverrideParameters:
    out: AssetBundleImportJobDataSetOverrideParameters = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSetOverrideParameters.data_set_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "DataSetRefreshProperties" in data:
        import aws_sdk_quicksight.types.data_set_refresh_properties

        out["data_set_refresh_properties"] = (
            aws_sdk_quicksight.types.data_set_refresh_properties.deserialize_json(
                data["DataSetRefreshProperties"]
            )
        )
    return out
