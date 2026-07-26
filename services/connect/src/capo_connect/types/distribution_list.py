"""Generated from Smithy shape ``com.amazonaws.connect#DistributionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.distribution

DistributionList: TypeAlias = list["capo_connect.types.distribution.Distribution"]


# --- restJson1 ser/de ---
def serialize_json(value: DistributionList) -> list:
    import capo_connect.types.distribution

    out: list = []
    for item in value:
        out.append(capo_connect.types.distribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> DistributionList:
    import capo_connect.types.distribution

    out: DistributionList = []
    for item in data:
        out.append(capo_connect.types.distribution.deserialize_json(item))
    return out
