"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.additional_analyses
    import aws_sdk_cleanrooms.types.analysis_rule_column_list
    import aws_sdk_cleanrooms.types.join_operators_list


class AnalysisRuleList(TypedDict):
    join_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.</p>"""
    allowed_join_operators: NotRequired[
        "aws_sdk_cleanrooms.types.join_operators_list.JoinOperatorsList"
    ]
    """<p>The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is <code>AND</code>.</p>"""
    list_columns: (
        "aws_sdk_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>Columns that can be listed in the output.</p>"""
    additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleList) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["join_columns"]
        )
    )
    if "allowed_join_operators" in value:
        import aws_sdk_cleanrooms.types.join_operators_list

        out["allowedJoinOperators"] = (
            aws_sdk_cleanrooms.types.join_operators_list.serialize_json(
                value["allowed_join_operators"]
            )
        )
    import aws_sdk_cleanrooms.types.analysis_rule_column_list

    out["listColumns"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["list_columns"]
        )
    )
    if "additional_analyses" in value:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleList:
    out: AnalysisRuleList = {}  # type: ignore[typeddict-item]
    if "joinColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleList.join_columns required")
    if "allowedJoinOperators" in data:
        import aws_sdk_cleanrooms.types.join_operators_list

        out["allowed_join_operators"] = (
            aws_sdk_cleanrooms.types.join_operators_list.deserialize_json(
                data["allowedJoinOperators"]
            )
        )
    if "listColumns" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_list

        out["list_columns"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["listColumns"]
            )
        )
    else:
        raise DeserializationError("AnalysisRuleList.list_columns required")
    if "additionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            aws_sdk_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    return out
