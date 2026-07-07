"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.configuration
    import aws_sdk_iottwinmaker.types.data_type
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.property_display_name


class PropertyDefinitionRequest(TypedDict, closed=True):
    data_type: NotRequired["aws_sdk_iottwinmaker.types.data_type.DataType"]
    """<p>An object that contains information about the data type.</p>"""
    is_required_in_entity: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the property is required.</p>"""
    is_external_id: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the property ID comes from an external data store.</p>"""
    is_stored_externally: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the property is stored externally.</p>"""
    is_time_series: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the property consists of time series data.</p>"""
    default_value: NotRequired["aws_sdk_iottwinmaker.types.data_value.DataValue"]
    """<p>An object that contains the default value.</p>"""
    configuration: NotRequired["aws_sdk_iottwinmaker.types.configuration.Configuration"]
    """<p>A mapping that specifies configuration information about the property. Use this field to specify information that you read from and write to an external source.</p>"""
    display_name: NotRequired[
        "aws_sdk_iottwinmaker.types.property_display_name.PropertyDisplayName"
    ]
    """<p>A friendly name for the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyDefinitionRequest) -> dict:
    out: dict = {}
    if "data_type" in value:
        import aws_sdk_iottwinmaker.types.data_type

        out["dataType"] = aws_sdk_iottwinmaker.types.data_type.serialize_json(
            value["data_type"]
        )
    if "is_required_in_entity" in value:
        out["isRequiredInEntity"] = value["is_required_in_entity"]
    if "is_external_id" in value:
        out["isExternalId"] = value["is_external_id"]
    if "is_stored_externally" in value:
        out["isStoredExternally"] = value["is_stored_externally"]
    if "is_time_series" in value:
        out["isTimeSeries"] = value["is_time_series"]
    if "default_value" in value:
        import aws_sdk_iottwinmaker.types.data_value

        out["defaultValue"] = aws_sdk_iottwinmaker.types.data_value.serialize_json(
            value["default_value"]
        )
    if "configuration" in value:
        import aws_sdk_iottwinmaker.types.configuration

        out["configuration"] = aws_sdk_iottwinmaker.types.configuration.serialize_json(
            value["configuration"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> PropertyDefinitionRequest:
    out: PropertyDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "dataType" in data:
        import aws_sdk_iottwinmaker.types.data_type

        out["data_type"] = aws_sdk_iottwinmaker.types.data_type.deserialize_json(
            data["dataType"]
        )
    if "isRequiredInEntity" in data:
        out["is_required_in_entity"] = data["isRequiredInEntity"]
    if "isExternalId" in data:
        out["is_external_id"] = data["isExternalId"]
    if "isStoredExternally" in data:
        out["is_stored_externally"] = data["isStoredExternally"]
    if "isTimeSeries" in data:
        out["is_time_series"] = data["isTimeSeries"]
    if "defaultValue" in data:
        import aws_sdk_iottwinmaker.types.data_value

        out["default_value"] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(
            data["defaultValue"]
        )
    if "configuration" in data:
        import aws_sdk_iottwinmaker.types.configuration

        out["configuration"] = (
            aws_sdk_iottwinmaker.types.configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
