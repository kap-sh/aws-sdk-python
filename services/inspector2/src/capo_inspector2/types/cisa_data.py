"""Generated from Smithy shape ``com.amazonaws.inspector2#CisaData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cisa_action
    import capo_inspector2.types.cisa_date_added
    import capo_inspector2.types.cisa_date_due


class CisaData(TypedDict, closed=True):
    date_added: NotRequired["capo_inspector2.types.cisa_date_added.CisaDateAdded"]
    """<p>The date and time CISA added this vulnerability to their catalogue.</p>"""
    date_due: NotRequired["capo_inspector2.types.cisa_date_due.CisaDateDue"]
    """<p>The date and time CISA expects a fix to have been provided vulnerability.</p>"""
    action: NotRequired["capo_inspector2.types.cisa_action.CisaAction"]
    """<p>The remediation action recommended by CISA for this vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisaData) -> dict:
    out: dict = {}
    if "date_added" in value:
        import capo_inspector2.types.cisa_date_added

        out["dateAdded"] = capo_inspector2.types.cisa_date_added.serialize_json(
            value["date_added"]
        )
    if "date_due" in value:
        import capo_inspector2.types.cisa_date_due

        out["dateDue"] = capo_inspector2.types.cisa_date_due.serialize_json(
            value["date_due"]
        )
    if "action" in value:
        out["action"] = value["action"]
    return out


def deserialize_json(data: dict) -> CisaData:
    out: CisaData = {}  # type: ignore[typeddict-item]
    if "dateAdded" in data:
        import capo_inspector2.types.cisa_date_added

        out["date_added"] = capo_inspector2.types.cisa_date_added.deserialize_json(
            data["dateAdded"]
        )
    if "dateDue" in data:
        import capo_inspector2.types.cisa_date_due

        out["date_due"] = capo_inspector2.types.cisa_date_due.deserialize_json(
            data["dateDue"]
        )
    if "action" in data:
        out["action"] = data["action"]
    return out
