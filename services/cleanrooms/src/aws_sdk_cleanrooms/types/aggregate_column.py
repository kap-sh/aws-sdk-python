"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregateColumn``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.aggregate_function_name
    import aws_sdk_cleanrooms.types.analysis_rule_column_name_list


class AggregateColumn(TypedDict):
    column_names: "aws_sdk_cleanrooms.types.analysis_rule_column_name_list.AnalysisRuleColumnNameList"
    """<p>Column names in configured table of aggregate columns.</p>"""
    function: "aws_sdk_cleanrooms.types.aggregate_function_name.AggregateFunctionName"
    """<p>Aggregation function that can be applied to aggregate column in query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregateColumn) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_rule_column_name_list

    out["columnNames"] = (
        aws_sdk_cleanrooms.types.analysis_rule_column_name_list.serialize_json(
            value["column_names"]
        )
    )
    out["function"] = value["function"]
    return out


def deserialize_json(data: dict) -> AggregateColumn:
    out: AggregateColumn = {}  # type: ignore[typeddict-item]
    if "columnNames" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_column_name_list

        out["column_names"] = (
            aws_sdk_cleanrooms.types.analysis_rule_column_name_list.deserialize_json(
                data["columnNames"]
            )
        )
    else:
        raise DeserializationError("AggregateColumn.column_names required")
    if "function" in data:
        out["function"] = data["function"]
    else:
        raise DeserializationError("AggregateColumn.function required")
    return out
