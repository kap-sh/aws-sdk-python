"""Generated from Smithy shape ``com.amazonaws.sagemaker#StatusDetailsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.scheduler_config_component
    import capo_sagemaker.types.scheduler_resource_status

StatusDetailsMap: TypeAlias = dict[
    "capo_sagemaker.types.scheduler_config_component.SchedulerConfigComponent",
    "capo_sagemaker.types.scheduler_resource_status.SchedulerResourceStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: StatusDetailsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.scheduler_config_component
        import capo_sagemaker.types.scheduler_resource_status

        out[
            capo_sagemaker.types.scheduler_config_component.serialize_aws_json_1_1(key)
        ] = capo_sagemaker.types.scheduler_resource_status.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> StatusDetailsMap:
    out: StatusDetailsMap = {}
    for key, value in data.items():
        import capo_sagemaker.types.scheduler_config_component
        import capo_sagemaker.types.scheduler_resource_status

        out[
            capo_sagemaker.types.scheduler_config_component.deserialize_aws_json_1_1(
                key
            )
        ] = capo_sagemaker.types.scheduler_resource_status.deserialize_aws_json_1_1(
            value
        )
    return out
