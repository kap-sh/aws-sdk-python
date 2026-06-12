"""Generated from Smithy shape ``com.amazonaws.synthetics#DryRunConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.string
    import aws_sdk_synthetics.types.uuid


class DryRunConfigOutput(TypedDict):
    dry_run_id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>"""
    last_dry_run_execution_status: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>Returns the last execution status for a canary's dry run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DryRunConfigOutput) -> dict:
    out: dict = {}
    if "dry_run_id" in value:
        out["DryRunId"] = value["dry_run_id"]
    if "last_dry_run_execution_status" in value:
        out["LastDryRunExecutionStatus"] = value["last_dry_run_execution_status"]
    return out


def deserialize_json(data: dict) -> DryRunConfigOutput:
    out: DryRunConfigOutput = {}  # type: ignore[typeddict-item]
    if "DryRunId" in data:
        out["dry_run_id"] = data["DryRunId"]
    if "LastDryRunExecutionStatus" in data:
        out["last_dry_run_execution_status"] = data["LastDryRunExecutionStatus"]
    return out
