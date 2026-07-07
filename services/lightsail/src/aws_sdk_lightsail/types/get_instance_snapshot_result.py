"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_snapshot


class GetInstanceSnapshotResult(TypedDict, closed=True):
    instance_snapshot: NotRequired[
        "aws_sdk_lightsail.types.instance_snapshot.InstanceSnapshot"
    ]
    """<p>An array of key-value pairs containing information about the results of your get instance snapshot request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceSnapshotResult) -> dict:
    out: dict = {}
    if "instance_snapshot" in value:
        import aws_sdk_lightsail.types.instance_snapshot

        out["instanceSnapshot"] = (
            aws_sdk_lightsail.types.instance_snapshot.serialize_aws_json_1_1(
                value["instance_snapshot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceSnapshotResult:
    out: GetInstanceSnapshotResult = {}  # type: ignore[typeddict-item]
    if "instanceSnapshot" in data:
        import aws_sdk_lightsail.types.instance_snapshot

        out["instance_snapshot"] = (
            aws_sdk_lightsail.types.instance_snapshot.deserialize_aws_json_1_1(
                data["instanceSnapshot"]
            )
        )
    return out
