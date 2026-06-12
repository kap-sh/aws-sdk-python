"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute_configuration
    import aws_sdk_connect.types.predefined_attribute_name
    import aws_sdk_connect.types.predefined_attribute_purpose_name_list
    import aws_sdk_connect.types.predefined_attribute_values
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class PredefinedAttribute(TypedDict):
    name: NotRequired[
        "aws_sdk_connect.types.predefined_attribute_name.PredefinedAttributeName"
    ]
    """<p>The name of the predefined attribute.</p>"""
    values: NotRequired[
        "aws_sdk_connect.types.predefined_attribute_values.PredefinedAttributeValues"
    ]
    """<p>The values of the predefined attribute.</p>"""
    purposes: NotRequired[
        "aws_sdk_connect.types.predefined_attribute_purpose_name_list.PredefinedAttributePurposeNameList"
    ]
    """<p>Values that enable you to categorize your predefined attributes. You can use them in custom UI elements across the Connect Customer admin website.</p>"""
    attribute_configuration: NotRequired[
        "aws_sdk_connect.types.predefined_attribute_configuration.PredefinedAttributeConfiguration"
    ]
    """<p>Custom metadata that is associated to predefined attributes to control behavior in upstream services, such as controlling how a predefined attribute should be displayed in the Connect Customer admin website.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>Last modified time.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>Last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_connect.types.predefined_attribute_values

        out["Values"] = (
            aws_sdk_connect.types.predefined_attribute_values.serialize_json(
                value["values"]
            )
        )
    if "purposes" in value:
        import aws_sdk_connect.types.predefined_attribute_purpose_name_list

        out["Purposes"] = (
            aws_sdk_connect.types.predefined_attribute_purpose_name_list.serialize_json(
                value["purposes"]
            )
        )
    if "attribute_configuration" in value:
        import aws_sdk_connect.types.predefined_attribute_configuration

        out["AttributeConfiguration"] = (
            aws_sdk_connect.types.predefined_attribute_configuration.serialize_json(
                value["attribute_configuration"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> PredefinedAttribute:
    out: PredefinedAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_connect.types.predefined_attribute_values

        out["values"] = (
            aws_sdk_connect.types.predefined_attribute_values.deserialize_json(
                data["Values"]
            )
        )
    if "Purposes" in data:
        import aws_sdk_connect.types.predefined_attribute_purpose_name_list

        out["purposes"] = (
            aws_sdk_connect.types.predefined_attribute_purpose_name_list.deserialize_json(
                data["Purposes"]
            )
        )
    if "AttributeConfiguration" in data:
        import aws_sdk_connect.types.predefined_attribute_configuration

        out["attribute_configuration"] = (
            aws_sdk_connect.types.predefined_attribute_configuration.deserialize_json(
                data["AttributeConfiguration"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
