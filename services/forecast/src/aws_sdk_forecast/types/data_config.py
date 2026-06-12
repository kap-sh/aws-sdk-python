"""Generated from Smithy shape ``com.amazonaws.forecast#DataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.additional_datasets
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.attribute_configs


class DataConfig(TypedDict):
    dataset_group_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The ARN of the dataset group used to train the predictor.</p>"""
    attribute_configs: NotRequired[
        "aws_sdk_forecast.types.attribute_configs.AttributeConfigs"
    ]
    """<p>Aggregation and filling options for attributes in your dataset group.</p>"""
    additional_datasets: NotRequired[
        "aws_sdk_forecast.types.additional_datasets.AdditionalDatasets"
    ]
    """<p>Additional built-in datasets like Holidays and the Weather Index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataConfig) -> dict:
    out: dict = {}
    out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "attribute_configs" in value:
        import aws_sdk_forecast.types.attribute_configs

        out["AttributeConfigs"] = (
            aws_sdk_forecast.types.attribute_configs.serialize_aws_json_1_1(
                value["attribute_configs"]
            )
        )
    if "additional_datasets" in value:
        import aws_sdk_forecast.types.additional_datasets

        out["AdditionalDatasets"] = (
            aws_sdk_forecast.types.additional_datasets.serialize_aws_json_1_1(
                value["additional_datasets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataConfig:
    out: DataConfig = {}  # type: ignore[typeddict-item]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    else:
        raise DeserializationError("DataConfig.dataset_group_arn required")
    if "AttributeConfigs" in data:
        import aws_sdk_forecast.types.attribute_configs

        out["attribute_configs"] = (
            aws_sdk_forecast.types.attribute_configs.deserialize_aws_json_1_1(
                data["AttributeConfigs"]
            )
        )
    if "AdditionalDatasets" in data:
        import aws_sdk_forecast.types.additional_datasets

        out["additional_datasets"] = (
            aws_sdk_forecast.types.additional_datasets.deserialize_aws_json_1_1(
                data["AdditionalDatasets"]
            )
        )
    return out
