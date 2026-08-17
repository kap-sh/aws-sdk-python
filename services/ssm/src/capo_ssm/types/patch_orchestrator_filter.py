"""Generated from Smithy shape ``com.amazonaws.ssm#PatchOrchestratorFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.patch_orchestrator_filter_key
    import capo_ssm.types.patch_orchestrator_filter_values


class PatchOrchestratorFilter(TypedDict, closed=True):
    key: NotRequired[
        "capo_ssm.types.patch_orchestrator_filter_key.PatchOrchestratorFilterKey"
    ]
    """<p>The key for the filter.</p>"""
    values: NotRequired[
        "capo_ssm.types.patch_orchestrator_filter_values.PatchOrchestratorFilterValues"
    ]
    """<p>The value for the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchOrchestratorFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_ssm.types.patch_orchestrator_filter_values

        out["Values"] = (
            capo_ssm.types.patch_orchestrator_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchOrchestratorFilter:
    out: PatchOrchestratorFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Values") is not None:
        import capo_ssm.types.patch_orchestrator_filter_values

        out["values"] = (
            capo_ssm.types.patch_orchestrator_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
