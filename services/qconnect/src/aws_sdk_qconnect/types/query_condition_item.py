"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryConditionItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.query_condition_comparison_operator
    import aws_sdk_qconnect.types.query_condition_field_name


class QueryConditionItem(TypedDict):
    field: "aws_sdk_qconnect.types.query_condition_field_name.QueryConditionFieldName"
    """<p> The name of the field for query condition to query on.</p>"""
    comparator: "aws_sdk_qconnect.types.query_condition_comparison_operator.QueryConditionComparisonOperator"
    """<p>The comparison operator for query condition to query on.</p>"""
    value: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The value for the query condition to query on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryConditionItem) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["comparator"] = value["comparator"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> QueryConditionItem:
    out: QueryConditionItem = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    else:
        raise DeserializationError("QueryConditionItem.field required")
    if "comparator" in data:
        out["comparator"] = data["comparator"]
    else:
        raise DeserializationError("QueryConditionItem.comparator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("QueryConditionItem.value required")
    return out
