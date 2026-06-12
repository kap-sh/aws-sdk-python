"""Generated from Smithy shape ``com.amazonaws.memorydb#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.integer
    import aws_sdk_memorydb.types.string


class Endpoint(TypedDict):
    address: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The DNS hostname of the node.</p>"""
    port: "aws_sdk_memorydb.types.integer.Integer"
    """<p>The port number that the engine is listening on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    out["Port"] = value.get("port", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    return out
