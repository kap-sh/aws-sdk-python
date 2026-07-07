"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProblemTypeConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_classification_job_config
    import aws_sdk_sagemaker.types.tabular_job_config
    import aws_sdk_sagemaker.types.text_classification_job_config
    import aws_sdk_sagemaker.types.text_generation_job_config
    import aws_sdk_sagemaker.types.time_series_forecasting_job_config


class _AutoMLProblemTypeConfig_ImageClassificationJobConfig(TypedDict, closed=True):
    ImageClassificationJobConfig: "aws_sdk_sagemaker.types.image_classification_job_config.ImageClassificationJobConfig"


class _AutoMLProblemTypeConfig_TextClassificationJobConfig(TypedDict, closed=True):
    TextClassificationJobConfig: "aws_sdk_sagemaker.types.text_classification_job_config.TextClassificationJobConfig"


class _AutoMLProblemTypeConfig_TimeSeriesForecastingJobConfig(TypedDict, closed=True):
    TimeSeriesForecastingJobConfig: "aws_sdk_sagemaker.types.time_series_forecasting_job_config.TimeSeriesForecastingJobConfig"


class _AutoMLProblemTypeConfig_TabularJobConfig(TypedDict, closed=True):
    TabularJobConfig: "aws_sdk_sagemaker.types.tabular_job_config.TabularJobConfig"


class _AutoMLProblemTypeConfig_TextGenerationJobConfig(TypedDict, closed=True):
    TextGenerationJobConfig: (
        "aws_sdk_sagemaker.types.text_generation_job_config.TextGenerationJobConfig"
    )


AutoMLProblemTypeConfig: TypeAlias = (
    _AutoMLProblemTypeConfig_ImageClassificationJobConfig
    | _AutoMLProblemTypeConfig_TextClassificationJobConfig
    | _AutoMLProblemTypeConfig_TimeSeriesForecastingJobConfig
    | _AutoMLProblemTypeConfig_TabularJobConfig
    | _AutoMLProblemTypeConfig_TextGenerationJobConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLProblemTypeConfig) -> dict:
    if "ImageClassificationJobConfig" in value:
        import aws_sdk_sagemaker.types.image_classification_job_config

        return {
            "ImageClassificationJobConfig": aws_sdk_sagemaker.types.image_classification_job_config.serialize_aws_json_1_1(
                value["ImageClassificationJobConfig"]
            )
        }
    elif "TextClassificationJobConfig" in value:
        import aws_sdk_sagemaker.types.text_classification_job_config

        return {
            "TextClassificationJobConfig": aws_sdk_sagemaker.types.text_classification_job_config.serialize_aws_json_1_1(
                value["TextClassificationJobConfig"]
            )
        }
    elif "TimeSeriesForecastingJobConfig" in value:
        import aws_sdk_sagemaker.types.time_series_forecasting_job_config

        return {
            "TimeSeriesForecastingJobConfig": aws_sdk_sagemaker.types.time_series_forecasting_job_config.serialize_aws_json_1_1(
                value["TimeSeriesForecastingJobConfig"]
            )
        }
    elif "TabularJobConfig" in value:
        import aws_sdk_sagemaker.types.tabular_job_config

        return {
            "TabularJobConfig": aws_sdk_sagemaker.types.tabular_job_config.serialize_aws_json_1_1(
                value["TabularJobConfig"]
            )
        }
    elif "TextGenerationJobConfig" in value:
        import aws_sdk_sagemaker.types.text_generation_job_config

        return {
            "TextGenerationJobConfig": aws_sdk_sagemaker.types.text_generation_job_config.serialize_aws_json_1_1(
                value["TextGenerationJobConfig"]
            )
        }
    else:
        raise SerializationError("AutoMLProblemTypeConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AutoMLProblemTypeConfig:
    if "ImageClassificationJobConfig" in data:
        import aws_sdk_sagemaker.types.image_classification_job_config

        return {
            "ImageClassificationJobConfig": aws_sdk_sagemaker.types.image_classification_job_config.deserialize_aws_json_1_1(
                data["ImageClassificationJobConfig"]
            )
        }
    elif "TextClassificationJobConfig" in data:
        import aws_sdk_sagemaker.types.text_classification_job_config

        return {
            "TextClassificationJobConfig": aws_sdk_sagemaker.types.text_classification_job_config.deserialize_aws_json_1_1(
                data["TextClassificationJobConfig"]
            )
        }
    elif "TimeSeriesForecastingJobConfig" in data:
        import aws_sdk_sagemaker.types.time_series_forecasting_job_config

        return {
            "TimeSeriesForecastingJobConfig": aws_sdk_sagemaker.types.time_series_forecasting_job_config.deserialize_aws_json_1_1(
                data["TimeSeriesForecastingJobConfig"]
            )
        }
    elif "TabularJobConfig" in data:
        import aws_sdk_sagemaker.types.tabular_job_config

        return {
            "TabularJobConfig": aws_sdk_sagemaker.types.tabular_job_config.deserialize_aws_json_1_1(
                data["TabularJobConfig"]
            )
        }
    elif "TextGenerationJobConfig" in data:
        import aws_sdk_sagemaker.types.text_generation_job_config

        return {
            "TextGenerationJobConfig": aws_sdk_sagemaker.types.text_generation_job_config.deserialize_aws_json_1_1(
                data["TextGenerationJobConfig"]
            )
        }
    else:
        raise DeserializationError("AutoMLProblemTypeConfig: no recognized variant key")
