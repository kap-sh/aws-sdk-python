"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#PushConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_abort_config
    import aws_sdk_iot_managed_integrations.types.ota_task_execution_rollout_config
    import aws_sdk_iot_managed_integrations.types.ota_task_timeout_config


class PushConfig(TypedDict):
    abort_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_abort_config.OtaTaskAbortConfig"
    ]
    """<p>Structure representing one abort config.</p>"""
    rollout_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_execution_rollout_config.OtaTaskExecutionRolloutConfig"
    ]
    """<p>Structure representing one rollout config.</p>"""
    timeout_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_timeout_config.OtaTaskTimeoutConfig"
    ]
    """<p>Structure representing one timeout config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushConfig) -> dict:
    out: dict = {}
    if "abort_config" in value:
        import aws_sdk_iot_managed_integrations.types.ota_task_abort_config

        out["AbortConfig"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_abort_config.serialize_json(
                value["abort_config"]
            )
        )
    if "rollout_config" in value:
        import aws_sdk_iot_managed_integrations.types.ota_task_execution_rollout_config

        out["RolloutConfig"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_execution_rollout_config.serialize_json(
                value["rollout_config"]
            )
        )
    if "timeout_config" in value:
        import aws_sdk_iot_managed_integrations.types.ota_task_timeout_config

        out["TimeoutConfig"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_timeout_config.serialize_json(
                value["timeout_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushConfig:
    out: PushConfig = {}  # type: ignore[typeddict-item]
    if "AbortConfig" in data:
        import aws_sdk_iot_managed_integrations.types.ota_task_abort_config

        out["abort_config"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_abort_config.deserialize_json(
                data["AbortConfig"]
            )
        )
    if "RolloutConfig" in data:
        import aws_sdk_iot_managed_integrations.types.ota_task_execution_rollout_config

        out["rollout_config"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_execution_rollout_config.deserialize_json(
                data["RolloutConfig"]
            )
        )
    if "TimeoutConfig" in data:
        import aws_sdk_iot_managed_integrations.types.ota_task_timeout_config

        out["timeout_config"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_timeout_config.deserialize_json(
                data["TimeoutConfig"]
            )
        )
    return out
