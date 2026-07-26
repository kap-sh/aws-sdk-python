"""Generated from Smithy shape ``com.amazonaws.organizations#Handshakes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.handshake

Handshakes: TypeAlias = list["capo_organizations.types.handshake.Handshake"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Handshakes) -> list:
    import capo_organizations.types.handshake

    out: list = []
    for item in value:
        out.append(capo_organizations.types.handshake.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Handshakes:
    import capo_organizations.types.handshake

    out: Handshakes = []
    for item in data:
        out.append(capo_organizations.types.handshake.deserialize_aws_json_1_1(item))
    return out
