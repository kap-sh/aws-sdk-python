"""Generated from Smithy shape ``com.amazonaws.guardduty#GetMasterAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.master


class GetMasterAccountResponse(TypedDict, closed=True):
    master: NotRequired["capo_guardduty.types.master.Master"]
    """<p>The administrator account details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMasterAccountResponse) -> dict:
    out: dict = {}
    if "master" in value:
        import capo_guardduty.types.master

        out["master"] = capo_guardduty.types.master.serialize_json(value["master"])
    return out


def deserialize_json(data: dict) -> GetMasterAccountResponse:
    out: GetMasterAccountResponse = {}  # type: ignore[typeddict-item]
    if "master" in data:
        import capo_guardduty.types.master

        out["master"] = capo_guardduty.types.master.deserialize_json(data["master"])
    return out
