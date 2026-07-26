"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionRetryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.retry_config_criteria_list


class OtaTaskExecutionRetryConfig(TypedDict, closed=True):
    retry_config_criteria: NotRequired[
        "capo_iot_managed_integrations.types.retry_config_criteria_list.RetryConfigCriteriaList"
    ]
    """<p>The list of retry config criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskExecutionRetryConfig) -> dict:
    out: dict = {}
    if "retry_config_criteria" in value:
        import capo_iot_managed_integrations.types.retry_config_criteria_list

        out["RetryConfigCriteria"] = (
            capo_iot_managed_integrations.types.retry_config_criteria_list.serialize_json(
                value["retry_config_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> OtaTaskExecutionRetryConfig:
    out: OtaTaskExecutionRetryConfig = {}  # type: ignore[typeddict-item]
    if "RetryConfigCriteria" in data:
        import capo_iot_managed_integrations.types.retry_config_criteria_list

        out["retry_config_criteria"] = (
            capo_iot_managed_integrations.types.retry_config_criteria_list.deserialize_json(
                data["RetryConfigCriteria"]
            )
        )
    return out
