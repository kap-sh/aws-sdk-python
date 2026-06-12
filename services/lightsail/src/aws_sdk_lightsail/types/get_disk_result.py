"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.disk


class GetDiskResult(TypedDict):
    disk: NotRequired["aws_sdk_lightsail.types.disk.Disk"]
    """<p>An object containing information about the disk.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskResult) -> dict:
    out: dict = {}
    if "disk" in value:
        import aws_sdk_lightsail.types.disk

        out["disk"] = aws_sdk_lightsail.types.disk.serialize_aws_json_1_1(value["disk"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskResult:
    out: GetDiskResult = {}  # type: ignore[typeddict-item]
    if "disk" in data:
        import aws_sdk_lightsail.types.disk

        out["disk"] = aws_sdk_lightsail.types.disk.deserialize_aws_json_1_1(
            data["disk"]
        )
    return out
