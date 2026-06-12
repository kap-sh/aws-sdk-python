"""Generated from Smithy shape ``com.amazonaws.synthetics#GetCanaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_name
    import aws_sdk_synthetics.types.uuid


class GetCanaryRequest(TypedDict):
    name: "aws_sdk_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want details for.</p>"""
    dry_run_id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCanaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCanaryRequest:
    out: GetCanaryRequest = {}  # type: ignore[typeddict-item]
    return out
