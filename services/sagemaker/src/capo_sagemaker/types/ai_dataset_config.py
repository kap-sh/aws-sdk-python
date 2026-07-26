"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIDatasetConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_workload_input_data_config_list


class _AIDatasetConfig_InputDataConfig(TypedDict, closed=True):
    InputDataConfig: "capo_sagemaker.types.ai_workload_input_data_config_list.AIWorkloadInputDataConfigList"


AIDatasetConfig: TypeAlias = _AIDatasetConfig_InputDataConfig


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIDatasetConfig) -> dict:
    if "InputDataConfig" in value:
        import capo_sagemaker.types.ai_workload_input_data_config_list

        return {
            "InputDataConfig": capo_sagemaker.types.ai_workload_input_data_config_list.serialize_aws_json_1_1(
                value["InputDataConfig"]
            )
        }
    else:
        raise SerializationError("AIDatasetConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AIDatasetConfig:
    if "InputDataConfig" in data:
        import capo_sagemaker.types.ai_workload_input_data_config_list

        return {
            "InputDataConfig": capo_sagemaker.types.ai_workload_input_data_config_list.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        }
    else:
        raise DeserializationError("AIDatasetConfig: no recognized variant key")
