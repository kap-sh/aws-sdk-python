"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.analysis_method
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list
    import aws_sdk_cleanrooms.types.configured_table_arn
    import aws_sdk_cleanrooms.types.configured_table_identifier
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.selected_analysis_methods


class ConfiguredTableSummary(TypedDict):
    id: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    """<p>The unique ID of the configured table.</p>"""
    arn: "aws_sdk_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    """<p>The unique ARN of the configured table.</p>"""
    name: "aws_sdk_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the configured table.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table was last updated.</p>"""
    analysis_rule_types: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list.ConfiguredTableAnalysisRuleTypeList"
    """<p>The types of analysis rules associated with this configured table.</p>"""
    analysis_method: "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod"
    """<p>The analysis method for the configured tables. </p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the configured table summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
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
    if "selected_analysis_methods" in value:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTableSummary:
    out: ConfiguredTableSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfiguredTableSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfiguredTableSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredTableSummary.name required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableSummary.update_time required")
    if "analysisRuleTypes" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list

        out["analysis_rule_types"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredTableSummary.analysis_rule_types required"
        )
    if "analysisMethod" in data:
        import aws_sdk_cleanrooms.types.analysis_method

        out["analysis_method"] = (
            aws_sdk_cleanrooms.types.analysis_method.deserialize_json(
                data["analysisMethod"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableSummary.analysis_method required")
    if "selectedAnalysisMethods" in data:
        import aws_sdk_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            aws_sdk_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
