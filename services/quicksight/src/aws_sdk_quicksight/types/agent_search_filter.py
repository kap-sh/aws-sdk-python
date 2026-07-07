"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_ownership_filter_attribute
    import aws_sdk_quicksight.types.comparison_operator


class AgentSearchFilter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_quicksight.types.agent_ownership_filter_attribute.AgentOwnershipFilterAttribute"
    ]
    """<p>The name of the field to filter on.</p>"""
    operator: NotRequired[
        "aws_sdk_quicksight.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator to use for the filter.</p>"""
    value: NotRequired["str"]
    """<p>The value to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSearchFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_quicksight.types.agent_ownership_filter_attribute

        out["Name"] = (
            aws_sdk_quicksight.types.agent_ownership_filter_attribute.serialize_json(
                value["name"]
            )
        )
    if "operator" in value:
        import aws_sdk_quicksight.types.comparison_operator

        out["Operator"] = aws_sdk_quicksight.types.comparison_operator.serialize_json(
            value["operator"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AgentSearchFilter:
    out: AgentSearchFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_quicksight.types.agent_ownership_filter_attribute

        out["name"] = (
            aws_sdk_quicksight.types.agent_ownership_filter_attribute.deserialize_json(
                data["Name"]
            )
        )
    if "Operator" in data:
        import aws_sdk_quicksight.types.comparison_operator

        out["operator"] = aws_sdk_quicksight.types.comparison_operator.deserialize_json(
            data["Operator"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
