"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PublicKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.public_key_summary

PublicKeyList: TypeAlias = list[
    "capo_ivs_realtime.types.public_key_summary.PublicKeySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicKeyList) -> list:
    import capo_ivs_realtime.types.public_key_summary

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.public_key_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PublicKeyList:
    import capo_ivs_realtime.types.public_key_summary

    out: PublicKeyList = []
    for item in data:
        out.append(capo_ivs_realtime.types.public_key_summary.deserialize_json(item))
    return out
