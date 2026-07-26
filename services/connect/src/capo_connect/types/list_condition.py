"""Generated from Smithy shape ``com.amazonaws.connect#ListCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.conditions
    import capo_connect.types.target_list_type


class ListCondition(TypedDict, closed=True):
    target_list_type: NotRequired["capo_connect.types.target_list_type.TargetListType"]
    """<p>The type of target list that will be used to filter the users.</p>"""
    conditions: NotRequired["capo_connect.types.conditions.Conditions"]
    """<p>A list of Condition objects which would be applied together with an AND condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCondition) -> dict:
    out: dict = {}
    if "target_list_type" in value:
        import capo_connect.types.target_list_type

        out["TargetListType"] = capo_connect.types.target_list_type.serialize_json(
            value["target_list_type"]
        )
    if "conditions" in value:
        import capo_connect.types.conditions

        out["Conditions"] = capo_connect.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> ListCondition:
    out: ListCondition = {}  # type: ignore[typeddict-item]
    if "TargetListType" in data:
        import capo_connect.types.target_list_type

        out["target_list_type"] = capo_connect.types.target_list_type.deserialize_json(
            data["TargetListType"]
        )
    if "Conditions" in data:
        import capo_connect.types.conditions

        out["conditions"] = capo_connect.types.conditions.deserialize_json(
            data["Conditions"]
        )
    return out
