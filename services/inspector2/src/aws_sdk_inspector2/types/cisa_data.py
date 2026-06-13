"""Generated from Smithy shape ``com.amazonaws.inspector2#CisaData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cisa_action
    import aws_sdk_inspector2.types.cisa_date_added
    import aws_sdk_inspector2.types.cisa_date_due


class CisaData(TypedDict):
    date_added: NotRequired["aws_sdk_inspector2.types.cisa_date_added.CisaDateAdded"]
    """<p>The date and time CISA added this vulnerability to their catalogue.</p>"""
    date_due: NotRequired["aws_sdk_inspector2.types.cisa_date_due.CisaDateDue"]
    """<p>The date and time CISA expects a fix to have been provided vulnerability.</p>"""
    action: NotRequired["aws_sdk_inspector2.types.cisa_action.CisaAction"]
    """<p>The remediation action recommended by CISA for this vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisaData) -> dict:
    out: dict = {}
    if "date_added" in value:
        import aws_sdk_inspector2.types.cisa_date_added

        out["dateAdded"] = aws_sdk_inspector2.types.cisa_date_added.serialize_json(
            value["date_added"]
        )
    if "date_due" in value:
        import aws_sdk_inspector2.types.cisa_date_due

        out["dateDue"] = aws_sdk_inspector2.types.cisa_date_due.serialize_json(
            value["date_due"]
        )
    if "action" in value:
        out["action"] = value["action"]
    return out


def deserialize_json(data: dict) -> CisaData:
    out: CisaData = {}  # type: ignore[typeddict-item]
    if "dateAdded" in data:
        import aws_sdk_inspector2.types.cisa_date_added

        out["date_added"] = aws_sdk_inspector2.types.cisa_date_added.deserialize_json(
            data["dateAdded"]
        )
    if "dateDue" in data:
        import aws_sdk_inspector2.types.cisa_date_due

        out["date_due"] = aws_sdk_inspector2.types.cisa_date_due.deserialize_json(
            data["dateDue"]
        )
    if "action" in data:
        out["action"] = data["action"]
    return out
