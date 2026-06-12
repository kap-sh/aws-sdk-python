"""Generated from Smithy shape ``com.amazonaws.connect#DataTableAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.data_table_attribute_value_type
    import aws_sdk_connect.types.data_table_description
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.data_table_version
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.validation


class DataTableAttribute(TypedDict):
    attribute_id: NotRequired["aws_sdk_connect.types.data_table_id.DataTableId"]
    """<p>The unique identifier for the attribute within the data table.</p>"""
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The human-readable name of the attribute. Must be unique within the data table and conform to Connect naming standards.</p>"""
    value_type: "aws_sdk_connect.types.data_table_attribute_value_type.DataTableAttributeValueType"
    """<p>The type of value allowed for this attribute. Must be one of TEXT, TEXT_LIST, NUMBER, NUMBER_LIST, or BOOLEAN. Determines how values are validated and processed.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>An optional description explaining the purpose and usage of this attribute.</p>"""
    data_table_id: NotRequired["aws_sdk_connect.types.data_table_id.DataTableId"]
    """<p>The unique identifier of the data table that contains this attribute.</p>"""
    data_table_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the data table that contains this attribute.</p>"""
    primary: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Boolean indicating whether this attribute is used as a primary key for record identification. Primary attributes must have unique value combinations and cannot contain expressions.</p>"""
    version: NotRequired["aws_sdk_connect.types.data_table_version.DataTableVersion"]
    """<p>The version identifier for this attribute, used for versioning and change tracking.</p>"""
    lock_version: NotRequired[
        "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    ]
    """<p>The lock version for this attribute, used for optimistic locking to prevent concurrent modification conflicts.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this attribute was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this attribute was last modified, used for region replication.</p>"""
    validation: NotRequired["aws_sdk_connect.types.validation.Validation"]
    """<p>The validation rules applied to values of this attribute. Based on JSON Schema Draft 2020-12 with additional Connect-specific validations for data integrity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableAttribute) -> dict:
    out: dict = {}
    if "attribute_id" in value:
        out["AttributeId"] = value["attribute_id"]
    out["Name"] = value["name"]
    import aws_sdk_connect.types.data_table_attribute_value_type

    out["ValueType"] = (
        aws_sdk_connect.types.data_table_attribute_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "data_table_id" in value:
        out["DataTableId"] = value["data_table_id"]
    if "data_table_arn" in value:
        out["DataTableArn"] = value["data_table_arn"]
    out["Primary"] = value.get("primary", False)
    if "version" in value:
        out["Version"] = value["version"]
    if "lock_version" in value:
        import aws_sdk_connect.types.data_table_lock_version

        out["LockVersion"] = (
            aws_sdk_connect.types.data_table_lock_version.serialize_json(
                value["lock_version"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "validation" in value:
        import aws_sdk_connect.types.validation

        out["Validation"] = aws_sdk_connect.types.validation.serialize_json(
            value["validation"]
        )
    return out


def deserialize_json(data: dict) -> DataTableAttribute:
    out: DataTableAttribute = {}  # type: ignore[typeddict-item]
    if "AttributeId" in data:
        out["attribute_id"] = data["AttributeId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DataTableAttribute.name required")
    if "ValueType" in data:
        import aws_sdk_connect.types.data_table_attribute_value_type

        out["value_type"] = (
            aws_sdk_connect.types.data_table_attribute_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError("DataTableAttribute.value_type required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "DataTableId" in data:
        out["data_table_id"] = data["DataTableId"]
    if "DataTableArn" in data:
        out["data_table_arn"] = data["DataTableArn"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    if "Version" in data:
        out["version"] = data["Version"]
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "Validation" in data:
        import aws_sdk_connect.types.validation

        out["validation"] = aws_sdk_connect.types.validation.deserialize_json(
            data["Validation"]
        )
    return out
