"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyState``."""

from typing import Literal, TypeAlias, cast

ProxyState: TypeAlias = Literal[
    "ATTACHING",
    "ATTACHED",
    "DETACHING",
    "DETACHED",
    "ATTACH_FAILED",
    "DETACH_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProxyState:
    return cast(ProxyState, data)
