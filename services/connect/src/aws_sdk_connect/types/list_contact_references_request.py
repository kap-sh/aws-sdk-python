"""Generated from Smithy shape ``com.amazonaws.connect#ListContactReferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.reference_types


class ListContactReferencesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the initial contact.</p>"""
    reference_types: "aws_sdk_connect.types.reference_types.ReferenceTypes"
    """<p>The type of reference.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p> <important> <p>This is not expected to be set, because the value returned in the previous response is always null.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactReferencesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContactReferencesRequest:
    out: ListContactReferencesRequest = {}  # type: ignore[typeddict-item]
    return out
