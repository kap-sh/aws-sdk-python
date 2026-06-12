"""Generated from Smithy shape ``com.amazonaws.organizations#InviteAccountToOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshake


class InviteAccountToOrganizationResponse(TypedDict):
    handshake: NotRequired["aws_sdk_organizations.types.handshake.Handshake"]
    """<p>A structure that contains details about the handshake that is created to support this invitation request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InviteAccountToOrganizationResponse) -> dict:
    out: dict = {}
    if "handshake" in value:
        import aws_sdk_organizations.types.handshake

        out["Handshake"] = aws_sdk_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InviteAccountToOrganizationResponse:
    out: InviteAccountToOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "Handshake" in data:
        import aws_sdk_organizations.types.handshake

        out["handshake"] = (
            aws_sdk_organizations.types.handshake.deserialize_aws_json_1_1(
                data["Handshake"]
            )
        )
    return out
