"""Generated from Smithy shape ``com.amazonaws.iot#IotSiteWiseAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.put_asset_property_value_entry_list


class IotSiteWiseAction(TypedDict):
    put_asset_property_value_entries: "aws_sdk_iot.types.put_asset_property_value_entry_list.PutAssetPropertyValueEntryList"
    """<p>A list of asset property value entries.</p>"""
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants IoT permission to send an asset property value to IoT SiteWise. (<code>\"Action\": \"iotsitewise:BatchPutAssetPropertyValue\"</code>). The trust policy can restrict access to specific asset hierarchy paths.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseAction) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.put_asset_property_value_entry_list

    out["putAssetPropertyValueEntries"] = (
        aws_sdk_iot.types.put_asset_property_value_entry_list.serialize_json(
            value["put_asset_property_value_entries"]
        )
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IotSiteWiseAction:
    out: IotSiteWiseAction = {}  # type: ignore[typeddict-item]
    if "putAssetPropertyValueEntries" in data:
        import aws_sdk_iot.types.put_asset_property_value_entry_list

        out["put_asset_property_value_entries"] = (
            aws_sdk_iot.types.put_asset_property_value_entry_list.deserialize_json(
                data["putAssetPropertyValueEntries"]
            )
        )
    else:
        raise DeserializationError(
            "IotSiteWiseAction.put_asset_property_value_entries required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("IotSiteWiseAction.role_arn required")
    return out
