"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionSnapshotResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_resource_state
    import aws_sdk_imagebuilder.types.non_empty_string


class LifecycleExecutionSnapshotResource(TypedDict, closed=True):
    snapshot_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Identifies the impacted snapshot resource.</p>"""
    state: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_execution_resource_state.LifecycleExecutionResourceState"
    ]
    """<p>The runtime status of the lifecycle action taken for the snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionSnapshotResource) -> dict:
    out: dict = {}
    if "snapshot_id" in value:
        out["snapshotId"] = value["snapshot_id"]
    if "state" in value:
        import aws_sdk_imagebuilder.types.lifecycle_execution_resource_state

        out["state"] = (
            aws_sdk_imagebuilder.types.lifecycle_execution_resource_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifecycleExecutionSnapshotResource:
    out: LifecycleExecutionSnapshotResource = {}  # type: ignore[typeddict-item]
    if "snapshotId" in data:
        out["snapshot_id"] = data["snapshotId"]
    if "state" in data:
        import aws_sdk_imagebuilder.types.lifecycle_execution_resource_state

        out["state"] = (
            aws_sdk_imagebuilder.types.lifecycle_execution_resource_state.deserialize_json(
                data["state"]
            )
        )
    return out
