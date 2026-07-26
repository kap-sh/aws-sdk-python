"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAdministratorAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.invitation


class GetAdministratorAccountResponse(TypedDict, closed=True):
    administrator: NotRequired["capo_securityhub.types.invitation.Invitation"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAdministratorAccountResponse) -> dict:
    out: dict = {}
    if "administrator" in value:
        import capo_securityhub.types.invitation

        out["Administrator"] = capo_securityhub.types.invitation.serialize_json(
            value["administrator"]
        )
    return out


def deserialize_json(data: dict) -> GetAdministratorAccountResponse:
    out: GetAdministratorAccountResponse = {}  # type: ignore[typeddict-item]
    if "Administrator" in data:
        import capo_securityhub.types.invitation

        out["administrator"] = capo_securityhub.types.invitation.deserialize_json(
            data["Administrator"]
        )
    return out
