"""Generated from Smithy shape ``com.amazonaws.dax#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.integer
    import aws_sdk_dax.types.string


class Endpoint(TypedDict):
    address: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The DNS hostname of the endpoint.</p>"""
    port: "aws_sdk_dax.types.integer.Integer"
    """<p>The port number that applications should use to connect to the endpoint.</p>"""
    url: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The URL that applications should use to connect to the endpoint. The default ports are 8111 for the \"dax\" protocol and 9111 for the \"daxs\" protocol.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    out["Port"] = value.get("port", 0)
    if "url" in value:
        out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if "URL" in data:
        out["url"] = data["URL"]
    return out
