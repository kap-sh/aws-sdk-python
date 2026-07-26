"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskAbortConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.abort_config_criteria_list


class OtaTaskAbortConfig(TypedDict, closed=True):
    abort_config_criteria_list: NotRequired[
        "capo_iot_managed_integrations.types.abort_config_criteria_list.AbortConfigCriteriaList"
    ]
    """<p>The list of criteria for the abort config.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskAbortConfig) -> dict:
    out: dict = {}
    if "abort_config_criteria_list" in value:
        import capo_iot_managed_integrations.types.abort_config_criteria_list

        out["AbortConfigCriteriaList"] = (
            capo_iot_managed_integrations.types.abort_config_criteria_list.serialize_json(
                value["abort_config_criteria_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OtaTaskAbortConfig:
    out: OtaTaskAbortConfig = {}  # type: ignore[typeddict-item]
    if "AbortConfigCriteriaList" in data:
        import capo_iot_managed_integrations.types.abort_config_criteria_list

        out["abort_config_criteria_list"] = (
            capo_iot_managed_integrations.types.abort_config_criteria_list.deserialize_json(
                data["AbortConfigCriteriaList"]
            )
        )
    return out
