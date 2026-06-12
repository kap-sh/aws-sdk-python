"""Generated from Smithy shape ``com.amazonaws.connect#DistributionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.distribution

DistributionList: TypeAlias = list["aws_sdk_connect.types.distribution.Distribution"]


# --- restJson1 ser/de ---
def serialize_json(value: DistributionList) -> list:
    import aws_sdk_connect.types.distribution

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.distribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> DistributionList:
    import aws_sdk_connect.types.distribution

    out: DistributionList = []
    for item in data:
        out.append(aws_sdk_connect.types.distribution.deserialize_json(item))
    return out
