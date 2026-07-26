"""Generated from Smithy shape ``com.amazonaws.kinesis#MetricsNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.metrics_name

MetricsNameList: TypeAlias = list["capo_kinesis.types.metrics_name.MetricsName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsNameList) -> list:
    import capo_kinesis.types.metrics_name

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.metrics_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricsNameList:
    import capo_kinesis.types.metrics_name

    out: MetricsNameList = []
    for item in data:
        out.append(capo_kinesis.types.metrics_name.deserialize_aws_json_1_1(item))
    return out
