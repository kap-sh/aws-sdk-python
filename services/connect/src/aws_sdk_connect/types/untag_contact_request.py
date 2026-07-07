"""Generated from Smithy shape ``com.amazonaws.connect#UntagContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_tag_keys
    import aws_sdk_connect.types.instance_id


class UntagContactRequest(TypedDict, closed=True):
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tag_keys: "aws_sdk_connect.types.contact_tag_keys.ContactTagKeys"
    """<p>A list of tag keys. Existing tags on the contact whose keys are members of this list will be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagContactRequest:
    out: UntagContactRequest = {}  # type: ignore[typeddict-item]
    return out
