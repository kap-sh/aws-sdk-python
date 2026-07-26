"""Generated from Smithy shape ``com.amazonaws.pi#MetricQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.metric_query

MetricQueryList: TypeAlias = list["capo_pi.types.metric_query.MetricQuery"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricQueryList) -> list:
    import capo_pi.types.metric_query

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_query.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricQueryList:
    import capo_pi.types.metric_query

    out: MetricQueryList = []
    for item in data:
        out.append(capo_pi.types.metric_query.deserialize_aws_json_1_1(item))
    return out
