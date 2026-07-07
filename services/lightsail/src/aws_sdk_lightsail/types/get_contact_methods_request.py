"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContactMethodsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.contact_protocols_list


class GetContactMethodsRequest(TypedDict, closed=True):
    protocols: NotRequired[
        "aws_sdk_lightsail.types.contact_protocols_list.ContactProtocolsList"
    ]
    """<p>The protocols used to send notifications, such as <code>Email</code>, or <code>SMS</code> (text messaging).</p> <p>Specify a protocol in your request to return information about a specific contact method protocol.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactMethodsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactMethodsRequest:
    out: GetContactMethodsRequest = {}  # type: ignore[typeddict-item]
    return out
