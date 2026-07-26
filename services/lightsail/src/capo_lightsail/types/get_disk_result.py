"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.disk


class GetDiskResult(TypedDict, closed=True):
    disk: NotRequired["capo_lightsail.types.disk.Disk"]
    """<p>An object containing information about the disk.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskResult) -> dict:
    out: dict = {}
    if "disk" in value:
        import capo_lightsail.types.disk

        out["disk"] = capo_lightsail.types.disk.serialize_aws_json_1_1(value["disk"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskResult:
    out: GetDiskResult = {}  # type: ignore[typeddict-item]
    if "disk" in data:
        import capo_lightsail.types.disk

        out["disk"] = capo_lightsail.types.disk.deserialize_aws_json_1_1(data["disk"])
    return out
