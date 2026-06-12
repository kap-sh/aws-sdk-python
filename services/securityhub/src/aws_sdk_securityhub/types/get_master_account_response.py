"""Generated from Smithy shape ``com.amazonaws.securityhub#GetMasterAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.invitation


class GetMasterAccountResponse(TypedDict):
    master: NotRequired["aws_sdk_securityhub.types.invitation.Invitation"]
    """<p>A list of details about the Security Hub CSPM administrator account for the current member account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMasterAccountResponse) -> dict:
    out: dict = {}
    if "master" in value:
        import aws_sdk_securityhub.types.invitation

        out["Master"] = aws_sdk_securityhub.types.invitation.serialize_json(
            value["master"]
        )
    return out


def deserialize_json(data: dict) -> GetMasterAccountResponse:
    out: GetMasterAccountResponse = {}  # type: ignore[typeddict-item]
    if "Master" in data:
        import aws_sdk_securityhub.types.invitation

        out["master"] = aws_sdk_securityhub.types.invitation.deserialize_json(
            data["Master"]
        )
    return out
