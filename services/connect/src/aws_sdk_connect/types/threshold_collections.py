"""Generated from Smithy shape ``com.amazonaws.connect#ThresholdCollections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.threshold_v2

ThresholdCollections: TypeAlias = list["aws_sdk_connect.types.threshold_v2.ThresholdV2"]


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdCollections) -> list:
    import aws_sdk_connect.types.threshold_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.threshold_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThresholdCollections:
    import aws_sdk_connect.types.threshold_v2

    out: ThresholdCollections = []
    for item in data:
        out.append(aws_sdk_connect.types.threshold_v2.deserialize_json(item))
    return out
