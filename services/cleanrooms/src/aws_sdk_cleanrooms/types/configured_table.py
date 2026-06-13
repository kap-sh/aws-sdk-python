"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.allowed_column_list
    import aws_sdk_cleanrooms.types.analysis_method
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list
    import aws_sdk_cleanrooms.types.configured_table_arn
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.selected_analysis_methods
    import aws_sdk_cleanrooms.types.table_description
    import aws_sdk_cleanrooms.types.table_reference
    import aws_sdk_cleanrooms.types.uuid


class ConfiguredTable(TypedDict):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table.</p>"""
    arn: "aws_sdk_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    """<p>The unique ARN for the configured table.</p>"""
    name: "aws_sdk_cleanrooms.types.display_name.DisplayName"
    """<p>A name for the configured table.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.table_description.TableDescription"
    ]
    """<p>A description for the configured table.</p>"""
    table_reference: "aws_sdk_cleanrooms.types.table_reference.TableReference"
    """<p>The table that this configured table represents.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table was last updated</p>"""
    analysis_rule_types: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list.ConfiguredTableAnalysisRuleTypeList"
    """<p>The types of analysis rules associated with this configured table. Currently, only one analysis rule may be associated with a configured table.</p>"""
    analysis_method: "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod"
    """<p>The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    allowed_columns: "aws_sdk_cleanrooms.types.allowed_column_list.AllowedColumnList"
    """<p>The columns within the underlying Glue table that can be used within collaborations.</p>"""
    selected_analysis_methods: NotRequired[
        "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTable) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cleanrooms.types.table_reference

    out["tableReference"] = aws_sdk_cleanrooms.types.table_reference.serialize_json(
        value["table_reference"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list

    out["analysisRuleTypes"] = (
        aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list.serialize_json(
            value["analysis_rule_types"]
        )
    )
    import aws_sdk_cleanrooms.types.analysis_method

    out["analysisMethod"] = aws_sdk_cleanrooms.types.analysis_method.serialize_json(
        value["analysis_method"]
    )
    import aws_sdk_cleanrooms.types.allowed_column_list

    out["allowedColumns"] = aws_sdk_cleanrooms.types.allowed_column_list.serialize_json(
        value["allowed_columns"]
    )
    if "selected_analysis_methods" in value:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTable:
    out: ConfiguredTable = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfiguredTable.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfiguredTable.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredTable.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tableReference" in data:
        import aws_sdk_cleanrooms.types.table_reference

        out["table_reference"] = (
            aws_sdk_cleanrooms.types.table_reference.deserialize_json(
                data["tableReference"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTable.table_reference required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTable.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTable.update_time required")
    if "analysisRuleTypes" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list

        out["analysis_rule_types"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTable.analysis_rule_types required")
    if "analysisMethod" in data:
        import aws_sdk_cleanrooms.types.analysis_method

        out["analysis_method"] = (
            aws_sdk_cleanrooms.types.analysis_method.deserialize_json(
                data["analysisMethod"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTable.analysis_method required")
    if "allowedColumns" in data:
        import aws_sdk_cleanrooms.types.allowed_column_list

        out["allowed_columns"] = (
            aws_sdk_cleanrooms.types.allowed_column_list.deserialize_json(
                data["allowedColumns"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTable.allowed_columns required")
    if "selectedAnalysisMethods" in data:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
