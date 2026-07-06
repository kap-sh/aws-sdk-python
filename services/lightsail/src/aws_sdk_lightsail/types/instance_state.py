"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.string


class InstanceState(TypedDict, closed=True):
    code: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The status code for the instance.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The state of the instance (<code>running</code> or <code>pending</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceState) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceState:
    out: InstanceState = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "name" in data:
        out["name"] = data["name"]
    return out
