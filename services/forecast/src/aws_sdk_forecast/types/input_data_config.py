"""Generated from Smithy shape ``com.amazonaws.forecast#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.supplementary_features


class InputDataConfig(TypedDict, closed=True):
    dataset_group_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""
    supplementary_features: NotRequired[
        "aws_sdk_forecast.types.supplementary_features.SupplementaryFeatures"
    ]
    """<p>An array of supplementary features. The only supported feature is a holiday calendar.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> dict:
    out: dict = {}
    out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "supplementary_features" in value:
        import aws_sdk_forecast.types.supplementary_features

        out["SupplementaryFeatures"] = (
            aws_sdk_forecast.types.supplementary_features.serialize_aws_json_1_1(
                value["supplementary_features"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    else:
        raise DeserializationError("InputDataConfig.dataset_group_arn required")
    if "SupplementaryFeatures" in data:
        import aws_sdk_forecast.types.supplementary_features

        out["supplementary_features"] = (
            aws_sdk_forecast.types.supplementary_features.deserialize_aws_json_1_1(
                data["SupplementaryFeatures"]
            )
        )
    return out
