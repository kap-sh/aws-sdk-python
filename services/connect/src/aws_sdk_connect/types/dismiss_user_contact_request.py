"""Generated from Smithy shape ``com.amazonaws.connect#DismissUserContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.user_id


class DismissUserContactRequest(TypedDict, closed=True):
    user_id: "aws_sdk_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DismissUserContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> DismissUserContactRequest:
    out: DismissUserContactRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("DismissUserContactRequest.contact_id required")
    return out
