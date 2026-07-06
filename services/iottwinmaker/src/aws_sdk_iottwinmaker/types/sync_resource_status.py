"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncResourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.error_details
    import aws_sdk_iottwinmaker.types.sync_resource_state


class SyncResourceStatus(TypedDict, closed=True):
    state: NotRequired[
        "aws_sdk_iottwinmaker.types.sync_resource_state.SyncResourceState"
    ]
    """<p>The sync resource status state.</p>"""
    error: NotRequired["aws_sdk_iottwinmaker.types.error_details.ErrorDetails"]
    """<p>The status error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceStatus) -> dict:
    out: dict = {}
    if "state" in value:
        out["state"] = value["state"]
    if "error" in value:
        import aws_sdk_iottwinmaker.types.error_details

        out["error"] = aws_sdk_iottwinmaker.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> SyncResourceStatus:
    out: SyncResourceStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    if "error" in data:
        import aws_sdk_iottwinmaker.types.error_details

        out["error"] = aws_sdk_iottwinmaker.types.error_details.deserialize_json(
            data["error"]
        )
    return out
