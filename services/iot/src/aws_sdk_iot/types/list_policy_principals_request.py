"""Generated from Smithy shape ``com.amazonaws.iot#ListPolicyPrincipalsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ascending_order
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size
    import aws_sdk_iot.types.policy_name


class ListPolicyPrincipalsRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The result page size.</p>"""
    ascending_order: "aws_sdk_iot.types.ascending_order.AscendingOrder"
    """<p>Specifies the order for results. If true, the results are returned in ascending creation order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyPrincipalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyPrincipalsRequest:
    out: ListPolicyPrincipalsRequest = {}  # type: ignore[typeddict-item]
    return out
