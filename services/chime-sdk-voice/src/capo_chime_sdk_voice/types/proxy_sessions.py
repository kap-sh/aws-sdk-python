"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ProxySessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.proxy_session

ProxySessions: TypeAlias = list["capo_chime_sdk_voice.types.proxy_session.ProxySession"]


# --- restJson1 ser/de ---
def serialize_json(value: ProxySessions) -> list:
    import capo_chime_sdk_voice.types.proxy_session

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.proxy_session.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProxySessions:
    import capo_chime_sdk_voice.types.proxy_session

    out: ProxySessions = []
    for item in data:
        out.append(capo_chime_sdk_voice.types.proxy_session.deserialize_json(item))
    return out
