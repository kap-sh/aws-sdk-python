"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryDryRunConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.uuid


class CanaryDryRunConfigOutput(TypedDict, closed=True):
    dry_run_id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryDryRunConfigOutput) -> dict:
    out: dict = {}
    if "dry_run_id" in value:
        out["DryRunId"] = value["dry_run_id"]
    return out


def deserialize_json(data: dict) -> CanaryDryRunConfigOutput:
    out: CanaryDryRunConfigOutput = {}  # type: ignore[typeddict-item]
    if "DryRunId" in data:
        out["dry_run_id"] = data["DryRunId"]
    return out
