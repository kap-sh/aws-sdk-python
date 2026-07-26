"""Generated from Smithy shape ``com.amazonaws.budgets#Metrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.metric

Metrics: TypeAlias = list["capo_budgets.types.metric.Metric"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Metrics) -> list:
    import capo_budgets.types.metric

    out: list = []
    for item in value:
        out.append(capo_budgets.types.metric.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Metrics:
    import capo_budgets.types.metric

    out: Metrics = []
    for item in data:
        out.append(capo_budgets.types.metric.deserialize_aws_json_1_1(item))
    return out
