"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#HandshakeStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.handshake_status

HandshakeStatusList: TypeAlias = list[
    "capo_partnercentral_channel.types.handshake_status.HandshakeStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HandshakeStatusList) -> list:
    import capo_partnercentral_channel.types.handshake_status

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_channel.types.handshake_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> HandshakeStatusList:
    import capo_partnercentral_channel.types.handshake_status

    out: HandshakeStatusList = []
    for item in data:
        out.append(
            capo_partnercentral_channel.types.handshake_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
