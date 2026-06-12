"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ProxySessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.proxy_session

ProxySessions: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.proxy_session.ProxySession"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProxySessions) -> list:
    import aws_sdk_chime_sdk_voice.types.proxy_session

    out: list = []
    for item in value:
        out.append(aws_sdk_chime_sdk_voice.types.proxy_session.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProxySessions:
    import aws_sdk_chime_sdk_voice.types.proxy_session

    out: ProxySessions = []
    for item in data:
        out.append(aws_sdk_chime_sdk_voice.types.proxy_session.deserialize_json(item))
    return out
