"""Generated from Smithy shape ``com.amazonaws.synthetics#GetCanaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canary_name
    import capo_synthetics.types.uuid


class GetCanaryRequest(TypedDict, closed=True):
    name: "capo_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want details for.</p>"""
    dry_run_id: NotRequired["capo_synthetics.types.uuid.UUID"]
    """<p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCanaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCanaryRequest:
    out: GetCanaryRequest = {}  # type: ignore[typeddict-item]
    return out
