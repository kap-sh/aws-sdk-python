"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AcceptConnectionInvitationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection


class AcceptConnectionInvitationResponse(TypedDict, closed=True):
    connection: "capo_partnercentral_account.types.connection.Connection"
    """<p>The details of the accepted connection between the two partners.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptConnectionInvitationResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.connection

    out["Connection"] = (
        capo_partnercentral_account.types.connection.serialize_aws_json_1_0(
            value["connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptConnectionInvitationResponse:
    out: AcceptConnectionInvitationResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import capo_partnercentral_account.types.connection

        out["connection"] = (
            capo_partnercentral_account.types.connection.deserialize_aws_json_1_0(
                data["Connection"]
            )
        )
    else:
        raise DeserializationError(
            "AcceptConnectionInvitationResponse.connection required"
        )
    return out
