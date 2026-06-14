"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeParty``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshake_party_id
    import aws_sdk_organizations.types.handshake_party_type


class HandshakeParty(TypedDict):
    id: "aws_sdk_organizations.types.handshake_party_id.HandshakePartyId"
    r"""<p>ID for the participant: Acccount ID, organization ID, or email address.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for handshake ID string requires \"h-\" followed by from 8 to 32 lowercase letters or digits.</p>"""
    type: "aws_sdk_organizations.types.handshake_party_type.HandshakePartyType"
    """<p>The type of ID for the participant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeParty) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_organizations.types.handshake_party_type

    out["Type"] = (
        aws_sdk_organizations.types.handshake_party_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> HandshakeParty:
    out: HandshakeParty = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("HandshakeParty.id required")
    if "Type" in data:
        import aws_sdk_organizations.types.handshake_party_type

        out["type"] = (
            aws_sdk_organizations.types.handshake_party_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("HandshakeParty.type required")
    return out
