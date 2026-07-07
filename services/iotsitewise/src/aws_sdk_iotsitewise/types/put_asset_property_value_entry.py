"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutAssetPropertyValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_alias
    import aws_sdk_iotsitewise.types.asset_property_values
    import aws_sdk_iotsitewise.types.entry_id
    import aws_sdk_iotsitewise.types.id


class PutAssetPropertyValueEntry(TypedDict, closed=True):
    entry_id: "aws_sdk_iotsitewise.types.entry_id.EntryId"
    """<p>The user specified ID for the entry. You can use this ID to identify which entries failed.</p>"""
    asset_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset to update.</p>"""
    property_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property for this entry.</p>"""
    property_alias: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    r"""<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_values: (
        "aws_sdk_iotsitewise.types.asset_property_values.AssetPropertyValues"
    )
    """<p>The list of property values to upload. You can specify up to 10 <code>propertyValues</code> array elements. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetPropertyValueEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    import aws_sdk_iotsitewise.types.asset_property_values

    out["propertyValues"] = (
        aws_sdk_iotsitewise.types.asset_property_values.serialize_json(
            value["property_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutAssetPropertyValueEntry:
    out: PutAssetPropertyValueEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError("PutAssetPropertyValueEntry.entry_id required")
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    if "propertyAlias" in data:
        out["property_alias"] = data["propertyAlias"]
    if "propertyValues" in data:
        import aws_sdk_iotsitewise.types.asset_property_values

        out["property_values"] = (
            aws_sdk_iotsitewise.types.asset_property_values.deserialize_json(
                data["propertyValues"]
            )
        )
    else:
        raise DeserializationError(
            "PutAssetPropertyValueEntry.property_values required"
        )
    return out
