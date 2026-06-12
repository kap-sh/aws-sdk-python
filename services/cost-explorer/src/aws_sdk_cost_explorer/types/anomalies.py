"""Generated from Smithy shape ``com.amazonaws.costexplorer#Anomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly

Anomalies: TypeAlias = list["aws_sdk_cost_explorer.types.anomaly.Anomaly"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Anomalies) -> list:
    import aws_sdk_cost_explorer.types.anomaly

    out: list = []
    for item in value:
        out.append(aws_sdk_cost_explorer.types.anomaly.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Anomalies:
    import aws_sdk_cost_explorer.types.anomaly

    out: Anomalies = []
    for item in data:
        out.append(aws_sdk_cost_explorer.types.anomaly.deserialize_aws_json_1_1(item))
    return out
