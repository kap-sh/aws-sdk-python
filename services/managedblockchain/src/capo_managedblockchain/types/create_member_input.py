"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateMemberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.client_request_token_string
    import capo_managedblockchain.types.member_configuration
    import capo_managedblockchain.types.resource_id_string


class CreateMemberInput(TypedDict, closed=True):
    client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>"""
    invitation_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the invitation that is sent to the member to join the network.</p>"""
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network in which the member is created.</p>"""
    member_configuration: (
        "capo_managedblockchain.types.member_configuration.MemberConfiguration"
    )
    """<p>Member configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemberInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    out["InvitationId"] = value["invitation_id"]
    import capo_managedblockchain.types.member_configuration

    out["MemberConfiguration"] = (
        capo_managedblockchain.types.member_configuration.serialize_json(
            value["member_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMemberInput:
    out: CreateMemberInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateMemberInput.client_request_token required")
    if "InvitationId" in data:
        out["invitation_id"] = data["InvitationId"]
    else:
        raise DeserializationError("CreateMemberInput.invitation_id required")
    if "MemberConfiguration" in data:
        import capo_managedblockchain.types.member_configuration

        out["member_configuration"] = (
            capo_managedblockchain.types.member_configuration.deserialize_json(
                data["MemberConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateMemberInput.member_configuration required")
    return out
