"""Generated from Smithy shape ``com.amazonaws.ebs#CompleteSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ebs.types.status


class CompleteSnapshotResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_ebs.types.status.Status"]
    """<p>The status of the snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteSnapshotResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_ebs.types.status

        out["Status"] = aws_sdk_ebs.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CompleteSnapshotResponse:
    out: CompleteSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_ebs.types.status

        out["status"] = aws_sdk_ebs.types.status.deserialize_json(data["Status"])
    return out
