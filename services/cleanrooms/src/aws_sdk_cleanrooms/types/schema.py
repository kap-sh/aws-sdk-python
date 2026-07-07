"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Schema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.analysis_method
    import aws_sdk_cleanrooms.types.analysis_rule_type_list
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.column_list
    import aws_sdk_cleanrooms.types.schema_resource_arn
    import aws_sdk_cleanrooms.types.schema_status_detail_list
    import aws_sdk_cleanrooms.types.schema_type
    import aws_sdk_cleanrooms.types.schema_type_properties
    import aws_sdk_cleanrooms.types.selected_analysis_methods
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.table_description
    import aws_sdk_cleanrooms.types.uuid


class Schema(TypedDict, closed=True):
    columns: "aws_sdk_cleanrooms.types.column_list.ColumnList"
    """<p>The columns for the relation that this schema represents.</p>"""
    partition_keys: "aws_sdk_cleanrooms.types.column_list.ColumnList"
    """<p>The partition keys for the dataset underlying this schema.</p>"""
    analysis_rule_types: (
        "aws_sdk_cleanrooms.types.analysis_rule_type_list.AnalysisRuleTypeList"
    )
    """<p>The analysis rule types that are associated with the schema. Currently, only one entry is present.</p>"""
    analysis_method: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod"
    ]
    """<p>The analysis method for the schema. </p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the schema.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The unique account ID for the Amazon Web Services account that owns the schema.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>A name for the schema. The schema relation is referred to by this name when queried by a protected query.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the collaboration that the schema belongs to.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique Amazon Resource Name (ARN) for the collaboration that the schema belongs to.</p>"""
    description: "aws_sdk_cleanrooms.types.table_description.TableDescription"
    """<p>A description for the schema.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the schema was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the schema was updated.</p>"""
    type: "aws_sdk_cleanrooms.types.schema_type.SchemaType"
    """<p>The type of schema.</p>"""
    schema_status_details: (
        "aws_sdk_cleanrooms.types.schema_status_detail_list.SchemaStatusDetailList"
    )
    """<p>Details about the status of the schema. Currently, only one entry is present.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_cleanrooms.types.schema_resource_arn.SchemaResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the schema resource.</p>"""
    schema_type_properties: NotRequired[
        "aws_sdk_cleanrooms.types.schema_type_properties.SchemaTypeProperties"
    ]
    """<p>The schema type properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schema) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.column_list

    out["columns"] = aws_sdk_cleanrooms.types.column_list.serialize_json(
        value["columns"]
    )
    import aws_sdk_cleanrooms.types.column_list

    out["partitionKeys"] = aws_sdk_cleanrooms.types.column_list.serialize_json(
        value["partition_keys"]
    )
    import aws_sdk_cleanrooms.types.analysis_rule_type_list

    out["analysisRuleTypes"] = (
        aws_sdk_cleanrooms.types.analysis_rule_type_list.serialize_json(
            value["analysis_rule_types"]
        )
    )
    if "analysis_method" in value:
        import aws_sdk_cleanrooms.types.analysis_method

        out["analysisMethod"] = aws_sdk_cleanrooms.types.analysis_method.serialize_json(
            value["analysis_method"]
        )
    if "selected_analysis_methods" in value:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    out["creatorAccountId"] = value["creator_account_id"]
    out["name"] = value["name"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["description"] = value["description"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.schema_type

    out["type"] = aws_sdk_cleanrooms.types.schema_type.serialize_json(value["type"])
    import aws_sdk_cleanrooms.types.schema_status_detail_list

    out["schemaStatusDetails"] = (
        aws_sdk_cleanrooms.types.schema_status_detail_list.serialize_json(
            value.get("schema_status_details", [])
        )
    )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "schema_type_properties" in value:
        import aws_sdk_cleanrooms.types.schema_type_properties

        out["schemaTypeProperties"] = (
            aws_sdk_cleanrooms.types.schema_type_properties.serialize_json(
                value["schema_type_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Schema:
    out: Schema = {}  # type: ignore[typeddict-item]
    if "columns" in data:
        import aws_sdk_cleanrooms.types.column_list

        out["columns"] = aws_sdk_cleanrooms.types.column_list.deserialize_json(
            data["columns"]
        )
    else:
        raise DeserializationError("Schema.columns required")
    if "partitionKeys" in data:
        import aws_sdk_cleanrooms.types.column_list

        out["partition_keys"] = aws_sdk_cleanrooms.types.column_list.deserialize_json(
            data["partitionKeys"]
        )
    else:
        raise DeserializationError("Schema.partition_keys required")
    if "analysisRuleTypes" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_type_list

        out["analysis_rule_types"] = (
            aws_sdk_cleanrooms.types.analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    else:
        raise DeserializationError("Schema.analysis_rule_types required")
    if "analysisMethod" in data:
        import aws_sdk_cleanrooms.types.analysis_method

        out["analysis_method"] = (
            aws_sdk_cleanrooms.types.analysis_method.deserialize_json(
                data["analysisMethod"]
            )
        )
    if "selectedAnalysisMethods" in data:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError("Schema.creator_account_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Schema.name required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("Schema.collaboration_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("Schema.collaboration_arn required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("Schema.description required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("Schema.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("Schema.update_time required")
    if "type" in data:
        import aws_sdk_cleanrooms.types.schema_type

        out["type"] = aws_sdk_cleanrooms.types.schema_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("Schema.type required")
    if "schemaStatusDetails" in data:
        import aws_sdk_cleanrooms.types.schema_status_detail_list

        out["schema_status_details"] = (
            aws_sdk_cleanrooms.types.schema_status_detail_list.deserialize_json(
                data["schemaStatusDetails"]
            )
        )
    else:
        out["schema_status_details"] = []
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "schemaTypeProperties" in data:
        import aws_sdk_cleanrooms.types.schema_type_properties

        out["schema_type_properties"] = (
            aws_sdk_cleanrooms.types.schema_type_properties.deserialize_json(
                data["schemaTypeProperties"]
            )
        )
    return out
