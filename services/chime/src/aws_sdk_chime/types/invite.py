"""Generated from Smithy shape ``com.amazonaws.chime#Invite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.email_address
    import aws_sdk_chime.types.email_status
    import aws_sdk_chime.types.invite_status
    import aws_sdk_chime.types.string


class Invite(TypedDict, closed=True):
    invite_id: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The invite ID.</p>"""
    status: NotRequired["aws_sdk_chime.types.invite_status.InviteStatus"]
    """<p>The status of the invite.</p>"""
    email_address: NotRequired["aws_sdk_chime.types.email_address.EmailAddress"]
    """<p>The email address to which the invite is sent.</p>"""
    email_status: NotRequired["aws_sdk_chime.types.email_status.EmailStatus"]
    """<p>The status of the invite email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Invite) -> dict:
    out: dict = {}
    if "invite_id" in value:
        out["InviteId"] = value["invite_id"]
    if "status" in value:
        import aws_sdk_chime.types.invite_status

        out["Status"] = aws_sdk_chime.types.invite_status.serialize_json(
            value["status"]
        )
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "email_status" in value:
        import aws_sdk_chime.types.email_status

        out["EmailStatus"] = aws_sdk_chime.types.email_status.serialize_json(
            value["email_status"]
        )
    return out


def deserialize_json(data: dict) -> Invite:
    out: Invite = {}  # type: ignore[typeddict-item]
    if "InviteId" in data:
        out["invite_id"] = data["InviteId"]
    if "Status" in data:
        import aws_sdk_chime.types.invite_status

        out["status"] = aws_sdk_chime.types.invite_status.deserialize_json(
            data["Status"]
        )
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "EmailStatus" in data:
        import aws_sdk_chime.types.email_status

        out["email_status"] = aws_sdk_chime.types.email_status.deserialize_json(
            data["EmailStatus"]
        )
    return out
