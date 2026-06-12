"""Generated from Smithy shape ``com.amazonaws.connect#GetContactAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id


class GetContactAttributesRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    initial_contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the initial contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactAttributesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContactAttributesRequest:
    out: GetContactAttributesRequest = {}  # type: ignore[typeddict-item]
    return out
