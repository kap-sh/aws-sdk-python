"""Generated from Smithy shape ``com.amazonaws.mailmanager#Relays``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.relay

Relays: TypeAlias = list["aws_sdk_mailmanager.types.relay.Relay"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Relays) -> list:
    import aws_sdk_mailmanager.types.relay

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.relay.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Relays:
    import aws_sdk_mailmanager.types.relay

    out: Relays = []
    for item in data:
        out.append(aws_sdk_mailmanager.types.relay.deserialize_aws_json_1_0(item))
    return out
