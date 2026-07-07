"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.disk_snapshot


class GetDiskSnapshotResult(TypedDict, closed=True):
    disk_snapshot: NotRequired["aws_sdk_lightsail.types.disk_snapshot.DiskSnapshot"]
    """<p>An object containing information about the disk snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskSnapshotResult) -> dict:
    out: dict = {}
    if "disk_snapshot" in value:
        import aws_sdk_lightsail.types.disk_snapshot

        out["diskSnapshot"] = (
            aws_sdk_lightsail.types.disk_snapshot.serialize_aws_json_1_1(
                value["disk_snapshot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskSnapshotResult:
    out: GetDiskSnapshotResult = {}  # type: ignore[typeddict-item]
    if "diskSnapshot" in data:
        import aws_sdk_lightsail.types.disk_snapshot

        out["disk_snapshot"] = (
            aws_sdk_lightsail.types.disk_snapshot.deserialize_aws_json_1_1(
                data["diskSnapshot"]
            )
        )
    return out
