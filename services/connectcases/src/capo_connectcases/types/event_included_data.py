"""Generated from Smithy shape ``com.amazonaws.connectcases#EventIncludedData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_event_included_data
    import capo_connectcases.types.related_item_event_included_data


class EventIncludedData(TypedDict, closed=True):
    case_data: NotRequired[
        "capo_connectcases.types.case_event_included_data.CaseEventIncludedData"
    ]
    """<p>Details of what case data is published through the case event stream.</p>"""
    related_item_data: NotRequired[
        "capo_connectcases.types.related_item_event_included_data.RelatedItemEventIncludedData"
    ]
    """<p>Details of what related item data is published through the case event stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventIncludedData) -> dict:
    out: dict = {}
    if "case_data" in value:
        import capo_connectcases.types.case_event_included_data

        out["caseData"] = (
            capo_connectcases.types.case_event_included_data.serialize_json(
                value["case_data"]
            )
        )
    if "related_item_data" in value:
        import capo_connectcases.types.related_item_event_included_data

        out["relatedItemData"] = (
            capo_connectcases.types.related_item_event_included_data.serialize_json(
                value["related_item_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventIncludedData:
    out: EventIncludedData = {}  # type: ignore[typeddict-item]
    if "caseData" in data:
        import capo_connectcases.types.case_event_included_data

        out["case_data"] = (
            capo_connectcases.types.case_event_included_data.deserialize_json(
                data["caseData"]
            )
        )
    if "relatedItemData" in data:
        import capo_connectcases.types.related_item_event_included_data

        out["related_item_data"] = (
            capo_connectcases.types.related_item_event_included_data.deserialize_json(
                data["relatedItemData"]
            )
        )
    return out
