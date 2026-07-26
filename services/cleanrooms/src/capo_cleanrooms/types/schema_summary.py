"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.analysis_rule_type_list
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.schema_resource_arn
    import capo_cleanrooms.types.schema_type
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.uuid


class SchemaSummary(TypedDict, closed=True):
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name for the schema object.</p>"""
    type: "capo_cleanrooms.types.schema_type.SchemaType"
    """<p>The type of schema object.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The unique account ID for the Amazon Web Services account that owns the schema.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the schema object was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the schema object was last updated.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the collaboration that the schema belongs to.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the collaboration that the schema belongs to.</p>"""
    analysis_rule_types: (
        "capo_cleanrooms.types.analysis_rule_type_list.AnalysisRuleTypeList"
    )
    """<p>The types of analysis rules that are associated with this schema object.</p>"""
    analysis_method: NotRequired["capo_cleanrooms.types.analysis_method.AnalysisMethod"]
    """<p>The analysis method for the associated schema.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    resource_arn: NotRequired[
        "capo_cleanrooms.types.schema_resource_arn.SchemaResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the schema summary resource.</p>"""
    selected_analysis_methods: NotRequired[
        "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_cleanrooms.types.schema_type

    out["type"] = capo_cleanrooms.types.schema_type.serialize_json(value["type"])
    out["creatorAccountId"] = value["creator_account_id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    import capo_cleanrooms.types.analysis_rule_type_list

    out["analysisRuleTypes"] = (
        capo_cleanrooms.types.analysis_rule_type_list.serialize_json(
            value["analysis_rule_types"]
        )
    )
    if "analysis_method" in value:
        import capo_cleanrooms.types.analysis_method

        out["analysisMethod"] = capo_cleanrooms.types.analysis_method.serialize_json(
            value["analysis_method"]
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "selected_analysis_methods" in value:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            capo_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> SchemaSummary:
    out: SchemaSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SchemaSummary.name required")
    if "type" in data:
        import capo_cleanrooms.types.schema_type

        out["type"] = capo_cleanrooms.types.schema_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("SchemaSummary.type required")
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError("SchemaSummary.creator_account_id required")
    if "createTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("SchemaSummary.create_time required")
    if "updateTime" in data:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("SchemaSummary.update_time required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("SchemaSummary.collaboration_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("SchemaSummary.collaboration_arn required")
    if "analysisRuleTypes" in data:
        import capo_cleanrooms.types.analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    else:
        raise DeserializationError("SchemaSummary.analysis_rule_types required")
    if "analysisMethod" in data:
        import capo_cleanrooms.types.analysis_method

        out["analysis_method"] = capo_cleanrooms.types.analysis_method.deserialize_json(
            data["analysisMethod"]
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "selectedAnalysisMethods" in data:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            capo_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
