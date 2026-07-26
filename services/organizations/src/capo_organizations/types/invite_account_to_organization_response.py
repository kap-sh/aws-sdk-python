"""Generated from Smithy shape ``com.amazonaws.organizations#InviteAccountToOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake


class InviteAccountToOrganizationResponse(TypedDict, closed=True):
    handshake: NotRequired["capo_organizations.types.handshake.Handshake"]
    """<p>A structure that contains details about the handshake that is created to support this invitation request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InviteAccountToOrganizationResponse) -> dict:
    out: dict = {}
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["Handshake"] = capo_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InviteAccountToOrganizationResponse:
    out: InviteAccountToOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "Handshake" in data:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.deserialize_aws_json_1_1(
            data["Handshake"]
        )
    return out
