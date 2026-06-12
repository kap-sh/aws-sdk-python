"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyProfileFeatureObjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.anomaly_object

AnomalyProfileFeatureObjects: TypeAlias = list[
    "aws_sdk_guardduty.types.anomaly_object.AnomalyObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyProfileFeatureObjects) -> list:
    import aws_sdk_guardduty.types.anomaly_object

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.anomaly_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyProfileFeatureObjects:
    import aws_sdk_guardduty.types.anomaly_object

    out: AnomalyProfileFeatureObjects = []
    for item in data:
        out.append(aws_sdk_guardduty.types.anomaly_object.deserialize_json(item))
    return out
