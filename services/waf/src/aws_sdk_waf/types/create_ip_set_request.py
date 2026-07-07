"""Generated from Smithy shape ``com.amazonaws.waf#CreateIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.resource_name


class CreateIPSetRequest(TypedDict, closed=True):
    name: "aws_sdk_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>IPSet</a>. You can't change <code>Name</code> after you create the <code>IPSet</code>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIPSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIPSetRequest:
    out: CreateIPSetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateIPSetRequest.name required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("CreateIPSetRequest.change_token required")
    return out
