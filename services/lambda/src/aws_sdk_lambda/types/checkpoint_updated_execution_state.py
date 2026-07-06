"""Generated from Smithy shape ``com.amazonaws.lambda#CheckpointUpdatedExecutionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.operations
    import aws_sdk_lambda.types.string


class CheckpointUpdatedExecutionState(TypedDict, closed=True):
    operations: NotRequired["aws_sdk_lambda.types.operations.Operations"]
    """<p>A list of operations that have been updated since the last checkpoint.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Indicates that more results are available. Use this value in a subsequent call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckpointUpdatedExecutionState) -> dict:
    out: dict = {}
    if "operations" in value:
        import aws_sdk_lambda.types.operations

        out["Operations"] = aws_sdk_lambda.types.operations.serialize_json(
            value["operations"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> CheckpointUpdatedExecutionState:
    out: CheckpointUpdatedExecutionState = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import aws_sdk_lambda.types.operations

        out["operations"] = aws_sdk_lambda.types.operations.deserialize_json(
            data["Operations"]
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
