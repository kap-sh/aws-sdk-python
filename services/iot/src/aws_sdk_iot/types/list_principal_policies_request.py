"""Generated from Smithy shape ``com.amazonaws.iot#ListPrincipalPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size
    import aws_sdk_iot.types.principal


class ListPrincipalPoliciesRequest(TypedDict):
    principal: "aws_sdk_iot.types.principal.Principal"
    """<p>The principal. Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>), thingGroupArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:thinggroup/<i>groupName</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p>Specifies the order for results. If true, results are returned in ascending creation order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPrincipalPoliciesRequest:
    out: ListPrincipalPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
