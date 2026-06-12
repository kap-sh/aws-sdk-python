"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionRetryConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.retry_config_criteria_list


class OtaTaskExecutionRetryConfig(TypedDict):
    retry_config_criteria: NotRequired[
        "aws_sdk_iot_managed_integrations.types.retry_config_criteria_list.RetryConfigCriteriaList"
    ]
    """<p>The list of retry config criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskExecutionRetryConfig) -> dict:
    out: dict = {}
    if "retry_config_criteria" in value:
        import aws_sdk_iot_managed_integrations.types.retry_config_criteria_list

        out["RetryConfigCriteria"] = (
            aws_sdk_iot_managed_integrations.types.retry_config_criteria_list.serialize_json(
                value["retry_config_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> OtaTaskExecutionRetryConfig:
    out: OtaTaskExecutionRetryConfig = {}  # type: ignore[typeddict-item]
    if "RetryConfigCriteria" in data:
        import aws_sdk_iot_managed_integrations.types.retry_config_criteria_list

        out["retry_config_criteria"] = (
            aws_sdk_iot_managed_integrations.types.retry_config_criteria_list.deserialize_json(
                data["RetryConfigCriteria"]
            )
        )
    return out
