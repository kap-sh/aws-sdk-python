"""Generated from Smithy shape ``com.amazonaws.guardduty#GetAdministratorAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.administrator


class GetAdministratorAccountResponse(TypedDict, closed=True):
    administrator: NotRequired["capo_guardduty.types.administrator.Administrator"]
    """<p>The administrator account details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdministratorAccountResponse) -> dict:
    out: dict = {}
    if "administrator" in value:
        import capo_guardduty.types.administrator

        out["administrator"] = capo_guardduty.types.administrator.serialize_json(
            value["administrator"]
        )
    return out


def deserialize_json(data: dict) -> GetAdministratorAccountResponse:
    out: GetAdministratorAccountResponse = {}  # type: ignore[typeddict-item]
    if "administrator" in data:
        import capo_guardduty.types.administrator

        out["administrator"] = capo_guardduty.types.administrator.deserialize_json(
            data["administrator"]
        )
    return out
