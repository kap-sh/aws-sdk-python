"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.analysis_rule_policy
    import aws_sdk_cleanrooms.types.analysis_rule_type
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy
    import aws_sdk_cleanrooms.types.consolidated_policy
    import aws_sdk_cleanrooms.types.table_alias


class AnalysisRule(TypedDict, closed=True):
    collaboration_id: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique ID for the associated collaboration.</p>"""
    type: "aws_sdk_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    """<p>The type of analysis rule.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>The name for the analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the analysis rule was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the analysis rule was last updated.</p>"""
    policy: "aws_sdk_cleanrooms.types.analysis_rule_policy.AnalysisRulePolicy"
    """<p>A policy that describes the associated data usage limitations.</p>"""
    collaboration_policy: NotRequired[
        "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy"
    ]
    consolidated_policy: NotRequired[
        "aws_sdk_cleanrooms.types.consolidated_policy.ConsolidatedPolicy"
    ]
    """<p> The consolidated policy for the analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRule) -> dict:
    out: dict = {}
    out["collaborationId"] = value["collaboration_id"]
    import aws_sdk_cleanrooms.types.analysis_rule_type

    out["type"] = aws_sdk_cleanrooms.types.analysis_rule_type.serialize_json(
        value["type"]
    )
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.analysis_rule_policy

    out["policy"] = aws_sdk_cleanrooms.types.analysis_rule_policy.serialize_json(
        value["policy"]
    )
    if "collaboration_policy" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["collaborationPolicy"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.serialize_json(
                value["collaboration_policy"]
            )
        )
    if "consolidated_policy" in value:
        import aws_sdk_cleanrooms.types.consolidated_policy

        out["consolidatedPolicy"] = (
            aws_sdk_cleanrooms.types.consolidated_policy.serialize_json(
                value["consolidated_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRule:
    out: AnalysisRule = {}  # type: ignore[typeddict-item]
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("AnalysisRule.collaboration_id required")
    if "type" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_type

        out["type"] = aws_sdk_cleanrooms.types.analysis_rule_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("AnalysisRule.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AnalysisRule.name required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("AnalysisRule.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("AnalysisRule.update_time required")
    if "policy" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_policy

        out["policy"] = aws_sdk_cleanrooms.types.analysis_rule_policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("AnalysisRule.policy required")
    if "collaborationPolicy" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["collaboration_policy"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.deserialize_json(
                data["collaborationPolicy"]
            )
        )
    if "consolidatedPolicy" in data:
        import aws_sdk_cleanrooms.types.consolidated_policy

        out["consolidated_policy"] = (
            aws_sdk_cleanrooms.types.consolidated_policy.deserialize_json(
                data["consolidatedPolicy"]
            )
        )
    return out
