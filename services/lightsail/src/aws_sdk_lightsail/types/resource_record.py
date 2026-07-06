"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class ResourceRecord(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name of the record.</p>"""
    type: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The DNS record type.</p>"""
    value: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The value for the DNS record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceRecord) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceRecord:
    out: ResourceRecord = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "value" in data:
        out["value"] = data["value"]
    return out
