"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeParties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshake_party

HandshakeParties: TypeAlias = list[
    "aws_sdk_organizations.types.handshake_party.HandshakeParty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeParties) -> list:
    import aws_sdk_organizations.types.handshake_party

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.handshake_party.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HandshakeParties:
    import aws_sdk_organizations.types.handshake_party

    out: HandshakeParties = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.handshake_party.deserialize_aws_json_1_1(item)
        )
    return out
