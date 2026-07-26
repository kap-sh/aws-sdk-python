"""Generated from Smithy shape ``com.amazonaws.forecast#Datasets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.dataset_summary

Datasets: TypeAlias = list["capo_forecast.types.dataset_summary.DatasetSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datasets) -> list:
    import capo_forecast.types.dataset_summary

    out: list = []
    for item in value:
        out.append(capo_forecast.types.dataset_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Datasets:
    import capo_forecast.types.dataset_summary

    out: Datasets = []
    for item in data:
        out.append(capo_forecast.types.dataset_summary.deserialize_aws_json_1_1(item))
    return out
