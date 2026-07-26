"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetBlueprintOptimizationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_optimization_job_status
    import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration


class GetBlueprintOptimizationStatusResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_optimization_job_status.BlueprintOptimizationJobStatus"
    ]
    """Job Status."""
    error_type: NotRequired["str"]
    """Error Type."""
    error_message: NotRequired["str"]
    """Error Message."""
    output_configuration: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration"
    ]
    """Output configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlueprintOptimizationStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_bedrock_data_automation.types.blueprint_optimization_job_status

        out["status"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_job_status.serialize_json(
                value["status"]
            )
        )
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "output_configuration" in value:
        import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration

        out["outputConfiguration"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.serialize_json(
                value["output_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBlueprintOptimizationStatusResponse:
    out: GetBlueprintOptimizationStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_bedrock_data_automation.types.blueprint_optimization_job_status

        out["status"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_job_status.deserialize_json(
                data["status"]
            )
        )
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "outputConfiguration" in data:
        import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    return out
