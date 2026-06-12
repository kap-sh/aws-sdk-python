"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.data_table_attribute_value_type
    import aws_sdk_connect.types.data_table_description
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.validation


class UpdateDataTableAttributeRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The current name of the attribute to update. Used as an identifier since attribute names can be changed.</p>"""
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The new name for the attribute. Must conform to Connect human readable string specification and be unique within the data table.</p>"""
    value_type: "aws_sdk_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    """<p>The updated value type for the attribute. When changing value types, existing values are not deleted but may return default values if incompatible.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>The updated description for the attribute.</p>"""
    primary: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether the attribute should be treated as a primary key. Converting to primary attribute requires existing values to maintain uniqueness.</p>"""
    validation: NotRequired["aws_sdk_connect.types.validation.Validation"]
    """<p>The updated validation rules for the attribute. Changes do not affect existing values until they are modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableAttributeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_connect.types.data_table_attribute_value_type

    out["ValueType"] = (
        aws_sdk_connect.types.data_table_attribute_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["Primary"] = value.get("primary", False)
    if "validation" in value:
        import aws_sdk_connect.types.validation

        out["Validation"] = aws_sdk_connect.types.validation.serialize_json(
            value["validation"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDataTableAttributeRequest:
    out: UpdateDataTableAttributeRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataTableAttributeRequest.name required")
    if "ValueType" in data:
        import aws_sdk_connect.types.data_table_attribute_value_type

        out["value_type"] = (
            aws_sdk_connect.types.data_table_attribute_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTableAttributeRequest.value_type required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    if "Validation" in data:
        import aws_sdk_connect.types.validation

        out["validation"] = aws_sdk_connect.types.validation.deserialize_json(
            data["Validation"]
        )
    return out
