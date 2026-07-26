"""Generated from Smithy shape ``com.amazonaws.waf#HTTPHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.header_name
    import capo_waf.types.header_value


class HTTPHeader(TypedDict, closed=True):
    name: NotRequired["capo_waf.types.header_name.HeaderName"]
    """<p>The name of one of the headers in the sampled web request.</p>"""
    value: NotRequired["capo_waf.types.header_value.HeaderValue"]
    """<p>The value of one of the headers in the sampled web request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HTTPHeader) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HTTPHeader:
    out: HTTPHeader = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
