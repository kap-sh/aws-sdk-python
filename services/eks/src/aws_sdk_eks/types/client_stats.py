"""Generated from Smithy shape ``com.amazonaws.eks#ClientStats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.client_stat

ClientStats: TypeAlias = list["aws_sdk_eks.types.client_stat.ClientStat"]


# --- restJson1 ser/de ---
def serialize_json(value: ClientStats) -> list:
    import aws_sdk_eks.types.client_stat

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.client_stat.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClientStats:
    import aws_sdk_eks.types.client_stat

    out: ClientStats = []
    for item in data:
        out.append(aws_sdk_eks.types.client_stat.deserialize_json(item))
    return out
