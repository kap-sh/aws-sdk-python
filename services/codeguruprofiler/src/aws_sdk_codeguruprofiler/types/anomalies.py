"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Anomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.anomaly

Anomalies: TypeAlias = list["aws_sdk_codeguruprofiler.types.anomaly.Anomaly"]


# --- restJson1 ser/de ---
def serialize_json(value: Anomalies) -> list:
    import aws_sdk_codeguruprofiler.types.anomaly

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguruprofiler.types.anomaly.serialize_json(item))
    return out


def deserialize_json(data: list) -> Anomalies:
    import aws_sdk_codeguruprofiler.types.anomaly

    out: Anomalies = []
    for item in data:
        out.append(aws_sdk_codeguruprofiler.types.anomaly.deserialize_json(item))
    return out
