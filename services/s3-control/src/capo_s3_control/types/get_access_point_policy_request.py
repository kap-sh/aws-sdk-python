"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_point_name
    import capo_s3_control.types.account_id


class GetAccessPointPolicyRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified access point.</p>"""
    name: "capo_s3_control.types.access_point_name.AccessPointName"
    """<p>The name of the access point whose policy you want to retrieve.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointPolicyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAccessPointPolicyRequest:
    out: GetAccessPointPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
