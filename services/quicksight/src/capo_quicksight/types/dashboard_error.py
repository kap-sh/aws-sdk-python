"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_error_type
    import capo_quicksight.types.entity_list
    import capo_quicksight.types.non_empty_string


class DashboardError(TypedDict, closed=True):
    type: NotRequired["capo_quicksight.types.dashboard_error_type.DashboardErrorType"]
    """<p>Type.</p>"""
    message: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>Message.</p>"""
    violated_entities: NotRequired["capo_quicksight.types.entity_list.EntityList"]
    """<p>Lists the violated entities that caused the dashboard error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardError) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_quicksight.types.dashboard_error_type

        out["Type"] = capo_quicksight.types.dashboard_error_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "violated_entities" in value:
        import capo_quicksight.types.entity_list

        out["ViolatedEntities"] = capo_quicksight.types.entity_list.serialize_json(
            value["violated_entities"]
        )
    return out


def deserialize_json(data: dict) -> DashboardError:
    out: DashboardError = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_quicksight.types.dashboard_error_type

        out["type"] = capo_quicksight.types.dashboard_error_type.deserialize_json(
            data["Type"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ViolatedEntities" in data:
        import capo_quicksight.types.entity_list

        out["violated_entities"] = capo_quicksight.types.entity_list.deserialize_json(
            data["ViolatedEntities"]
        )
    return out
