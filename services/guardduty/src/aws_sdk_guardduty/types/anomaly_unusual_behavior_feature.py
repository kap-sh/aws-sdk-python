"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyUnusualBehaviorFeature``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.anomaly_object
    import aws_sdk_guardduty.types.string

AnomalyUnusualBehaviorFeature: TypeAlias = dict[
    "aws_sdk_guardduty.types.string.String",
    "aws_sdk_guardduty.types.anomaly_object.AnomalyObject",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AnomalyUnusualBehaviorFeature) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_guardduty.types.anomaly_object

        out[key] = aws_sdk_guardduty.types.anomaly_object.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AnomalyUnusualBehaviorFeature:
    out: AnomalyUnusualBehaviorFeature = {}
    for key, value in data.items():
        import aws_sdk_guardduty.types.anomaly_object

        out[key] = aws_sdk_guardduty.types.anomaly_object.deserialize_json(value)
    return out
