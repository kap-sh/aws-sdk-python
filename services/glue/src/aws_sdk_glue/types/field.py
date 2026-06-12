"""Generated from Smithy shape ``com.amazonaws.glue#Field``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.bool
    import aws_sdk_glue.types.custom_properties
    import aws_sdk_glue.types.entity_field_name
    import aws_sdk_glue.types.field_data_type
    import aws_sdk_glue.types.field_description
    import aws_sdk_glue.types.field_filter_operators_list
    import aws_sdk_glue.types.field_label
    import aws_sdk_glue.types.list_of_string


class Field(TypedDict):
    field_name: NotRequired["aws_sdk_glue.types.entity_field_name.EntityFieldName"]
    """<p>A unique identifier for the field.</p>"""
    label: NotRequired["aws_sdk_glue.types.field_label.FieldLabel"]
    """<p>A readable label used for the field.</p>"""
    description: NotRequired["aws_sdk_glue.types.field_description.FieldDescription"]
    """<p>A description of the field.</p>"""
    field_type: NotRequired["aws_sdk_glue.types.field_data_type.FieldDataType"]
    """<p>The type of data in the field.</p>"""
    is_primary_key: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field can used as a primary key for the given entity.</p>"""
    is_nullable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be nullable or not.</p>"""
    is_retrievable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be added in Select clause of SQL query or whether it is retrievable or not.</p>"""
    is_filterable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p> Indicates whether this field can used in a filter clause (<code>WHERE</code> clause) of a SQL statement when querying data. </p>"""
    is_partitionable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether a given field can be used in partitioning the query made to SaaS.</p>"""
    is_createable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be created as part of a destination write.</p>"""
    is_updateable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be updated as part of a destination write.</p>"""
    is_upsertable: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be upserted as part of a destination write.</p>"""
    is_default_on_create: NotRequired["aws_sdk_glue.types.bool.Bool"]
    """<p>Indicates whether this field is populated automatically when the object is created, such as a created at timestamp.</p>"""
    supported_values: NotRequired["aws_sdk_glue.types.list_of_string.ListOfString"]
    """<p>A list of supported values for the field.</p>"""
    supported_filter_operators: NotRequired[
        "aws_sdk_glue.types.field_filter_operators_list.FieldFilterOperatorsList"
    ]
    """<p>Indicates the support filter operators for this field.</p>"""
    parent_field: NotRequired["str"]
    """<p>A parent field name for a nested field.</p>"""
    native_data_type: NotRequired["str"]
    """<p>The data type returned by the SaaS API, such as “picklist” or “textarea” from Salesforce.</p>"""
    custom_properties: NotRequired[
        "aws_sdk_glue.types.custom_properties.CustomProperties"
    ]
    """<p>Optional map of keys which may be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Field) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "label" in value:
        out["Label"] = value["label"]
    if "description" in value:
        out["Description"] = value["description"]
    if "field_type" in value:
        import aws_sdk_glue.types.field_data_type

        out["FieldType"] = aws_sdk_glue.types.field_data_type.serialize_aws_json_1_1(
            value["field_type"]
        )
    if "is_primary_key" in value:
        out["IsPrimaryKey"] = value["is_primary_key"]
    if "is_nullable" in value:
        out["IsNullable"] = value["is_nullable"]
    if "is_retrievable" in value:
        out["IsRetrievable"] = value["is_retrievable"]
    if "is_filterable" in value:
        out["IsFilterable"] = value["is_filterable"]
    if "is_partitionable" in value:
        out["IsPartitionable"] = value["is_partitionable"]
    if "is_createable" in value:
        out["IsCreateable"] = value["is_createable"]
    if "is_updateable" in value:
        out["IsUpdateable"] = value["is_updateable"]
    if "is_upsertable" in value:
        out["IsUpsertable"] = value["is_upsertable"]
    if "is_default_on_create" in value:
        out["IsDefaultOnCreate"] = value["is_default_on_create"]
    if "supported_values" in value:
        import aws_sdk_glue.types.list_of_string

        out["SupportedValues"] = (
            aws_sdk_glue.types.list_of_string.serialize_aws_json_1_1(
                value["supported_values"]
            )
        )
    if "supported_filter_operators" in value:
        import aws_sdk_glue.types.field_filter_operators_list

        out["SupportedFilterOperators"] = (
            aws_sdk_glue.types.field_filter_operators_list.serialize_aws_json_1_1(
                value["supported_filter_operators"]
            )
        )
    if "parent_field" in value:
        out["ParentField"] = value["parent_field"]
    if "native_data_type" in value:
        out["NativeDataType"] = value["native_data_type"]
    if "custom_properties" in value:
        import aws_sdk_glue.types.custom_properties

        out["CustomProperties"] = (
            aws_sdk_glue.types.custom_properties.serialize_aws_json_1_1(
                value["custom_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Field:
    out: Field = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "Label" in data:
        out["label"] = data["Label"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "FieldType" in data:
        import aws_sdk_glue.types.field_data_type

        out["field_type"] = aws_sdk_glue.types.field_data_type.deserialize_aws_json_1_1(
            data["FieldType"]
        )
    if "IsPrimaryKey" in data:
        out["is_primary_key"] = data["IsPrimaryKey"]
    if "IsNullable" in data:
        out["is_nullable"] = data["IsNullable"]
    if "IsRetrievable" in data:
        out["is_retrievable"] = data["IsRetrievable"]
    if "IsFilterable" in data:
        out["is_filterable"] = data["IsFilterable"]
    if "IsPartitionable" in data:
        out["is_partitionable"] = data["IsPartitionable"]
    if "IsCreateable" in data:
        out["is_createable"] = data["IsCreateable"]
    if "IsUpdateable" in data:
        out["is_updateable"] = data["IsUpdateable"]
    if "IsUpsertable" in data:
        out["is_upsertable"] = data["IsUpsertable"]
    if "IsDefaultOnCreate" in data:
        out["is_default_on_create"] = data["IsDefaultOnCreate"]
    if "SupportedValues" in data:
        import aws_sdk_glue.types.list_of_string

        out["supported_values"] = (
            aws_sdk_glue.types.list_of_string.deserialize_aws_json_1_1(
                data["SupportedValues"]
            )
        )
    if "SupportedFilterOperators" in data:
        import aws_sdk_glue.types.field_filter_operators_list

        out["supported_filter_operators"] = (
            aws_sdk_glue.types.field_filter_operators_list.deserialize_aws_json_1_1(
                data["SupportedFilterOperators"]
            )
        )
    if "ParentField" in data:
        out["parent_field"] = data["ParentField"]
    if "NativeDataType" in data:
        out["native_data_type"] = data["NativeDataType"]
    if "CustomProperties" in data:
        import aws_sdk_glue.types.custom_properties

        out["custom_properties"] = (
            aws_sdk_glue.types.custom_properties.deserialize_aws_json_1_1(
                data["CustomProperties"]
            )
        )
    return out
