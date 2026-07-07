"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAdministratorAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.invitation


class GetAdministratorAccountResponse(TypedDict, closed=True):
    administrator: NotRequired["aws_sdk_securityhub.types.invitation.Invitation"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAdministratorAccountResponse) -> dict:
    out: dict = {}
    if "administrator" in value:
        import aws_sdk_securityhub.types.invitation

        out["Administrator"] = aws_sdk_securityhub.types.invitation.serialize_json(
            value["administrator"]
        )
    return out


def deserialize_json(data: dict) -> GetAdministratorAccountResponse:
    out: GetAdministratorAccountResponse = {}  # type: ignore[typeddict-item]
    if "Administrator" in data:
        import aws_sdk_securityhub.types.invitation

        out["administrator"] = aws_sdk_securityhub.types.invitation.deserialize_json(
            data["Administrator"]
        )
    return out
