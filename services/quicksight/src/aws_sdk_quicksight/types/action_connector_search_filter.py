"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_search_filter_name_enum
    import aws_sdk_quicksight.types.filter_operator


class ActionConnectorSearchFilter(TypedDict, closed=True):
    name: "aws_sdk_quicksight.types.action_connector_search_filter_name_enum.ActionConnectorSearchFilterNameEnum"
    """<p>The name of the filter attribute (e.g., ACTION_CONNECTOR_NAME, ACTION_CONNECTOR_TYPE, QUICKSIGHT_VIEWER_OR_OWNER).</p>"""
    operator: "aws_sdk_quicksight.types.filter_operator.FilterOperator"
    """<p>The comparison operator to use for the filter (e.g., StringEquals, StringLike).</p>"""
    value: "str"
    """<p>The value to compare against using the specified operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSearchFilter) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.action_connector_search_filter_name_enum

    out["Name"] = (
        aws_sdk_quicksight.types.action_connector_search_filter_name_enum.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_quicksight.types.filter_operator

    out["Operator"] = aws_sdk_quicksight.types.filter_operator.serialize_json(
        value["operator"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ActionConnectorSearchFilter:
    out: ActionConnectorSearchFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_quicksight.types.action_connector_search_filter_name_enum

        out["name"] = (
            aws_sdk_quicksight.types.action_connector_search_filter_name_enum.deserialize_json(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("ActionConnectorSearchFilter.name required")
    if "Operator" in data:
        import aws_sdk_quicksight.types.filter_operator

        out["operator"] = aws_sdk_quicksight.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        raise DeserializationError("ActionConnectorSearchFilter.operator required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ActionConnectorSearchFilter.value required")
    return out
