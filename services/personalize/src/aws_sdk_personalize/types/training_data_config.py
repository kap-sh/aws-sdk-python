"""Generated from Smithy shape ``com.amazonaws.personalize#TrainingDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.excluded_dataset_columns
    import aws_sdk_personalize.types.included_dataset_columns


class TrainingDataConfig(TypedDict):
    excluded_dataset_columns: NotRequired[
        "aws_sdk_personalize.types.excluded_dataset_columns.ExcludedDatasetColumns"
    ]
    """<p>Specifies the columns to exclude from training. Each key is a dataset type, and each value is a list of columns. Exclude columns to control what data Amazon Personalize uses to generate recommendations.</p> <p> For example, you might have a column that you want to use only to filter recommendations. You can exclude this column from training and Amazon Personalize considers it only when filtering. </p>"""
    included_dataset_columns: NotRequired[
        "aws_sdk_personalize.types.included_dataset_columns.IncludedDatasetColumns"
    ]
    """<p>A map that specifies which columns to include from each dataset during training. The map can contain up to 3 entries, where each key is a dataset name (maximum length of 256 characters, must contain only letters and underscores) and each value is an array of up to 50 column names. Column names can be up to 150 characters long, must start with a letter or underscore, and can contain only letters, numbers, and underscores.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingDataConfig) -> dict:
    out: dict = {}
    if "excluded_dataset_columns" in value:
        import aws_sdk_personalize.types.excluded_dataset_columns

        out["excludedDatasetColumns"] = (
            aws_sdk_personalize.types.excluded_dataset_columns.serialize_aws_json_1_1(
                value["excluded_dataset_columns"]
            )
        )
    if "included_dataset_columns" in value:
        import aws_sdk_personalize.types.included_dataset_columns

        out["includedDatasetColumns"] = (
            aws_sdk_personalize.types.included_dataset_columns.serialize_aws_json_1_1(
                value["included_dataset_columns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingDataConfig:
    out: TrainingDataConfig = {}  # type: ignore[typeddict-item]
    if "excludedDatasetColumns" in data:
        import aws_sdk_personalize.types.excluded_dataset_columns

        out["excluded_dataset_columns"] = (
            aws_sdk_personalize.types.excluded_dataset_columns.deserialize_aws_json_1_1(
                data["excludedDatasetColumns"]
            )
        )
    if "includedDatasetColumns" in data:
        import aws_sdk_personalize.types.included_dataset_columns

        out["included_dataset_columns"] = (
            aws_sdk_personalize.types.included_dataset_columns.deserialize_aws_json_1_1(
                data["includedDatasetColumns"]
            )
        )
    return out
