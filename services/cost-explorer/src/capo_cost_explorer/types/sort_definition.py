"""Generated from Smithy shape ``com.amazonaws.costexplorer#SortDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.sort_definition_key
    import capo_cost_explorer.types.sort_order


class SortDefinition(TypedDict, closed=True):
    key: "capo_cost_explorer.types.sort_definition_key.SortDefinitionKey"
    """<p>The key that's used to sort the data.</p>"""
    sort_order: NotRequired["capo_cost_explorer.types.sort_order.SortOrder"]
    """<p>The order that's used to sort the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortDefinition) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "sort_order" in value:
        import capo_cost_explorer.types.sort_order

        out["SortOrder"] = capo_cost_explorer.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SortDefinition:
    out: SortDefinition = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("SortDefinition.key required")
    if "SortOrder" in data:
        import capo_cost_explorer.types.sort_order

        out["sort_order"] = (
            capo_cost_explorer.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out
