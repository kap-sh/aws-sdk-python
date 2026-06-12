"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AnomalyInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.anomaly_instance

AnomalyInstances: TypeAlias = list[
    "aws_sdk_codeguruprofiler.types.anomaly_instance.AnomalyInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyInstances) -> list:
    import aws_sdk_codeguruprofiler.types.anomaly_instance

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguruprofiler.types.anomaly_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnomalyInstances:
    import aws_sdk_codeguruprofiler.types.anomaly_instance

    out: AnomalyInstances = []
    for item in data:
        out.append(
            aws_sdk_codeguruprofiler.types.anomaly_instance.deserialize_json(item)
        )
    return out
