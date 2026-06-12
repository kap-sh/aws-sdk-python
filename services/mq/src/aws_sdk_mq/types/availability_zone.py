"""Generated from Smithy shape ``com.amazonaws.mq#AvailabilityZone``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class AvailabilityZone(TypedDict):
    name: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Id for the availability zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZone) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
