"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointPolicyStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_point_name
    import capo_s3_control.types.account_id


class GetAccessPointPolicyStatusRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified access point.</p>"""
    name: "capo_s3_control.types.access_point_name.AccessPointName"
    """<p>The name of the access point whose policy status you want to retrieve.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointPolicyStatusRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAccessPointPolicyStatusRequest:
    out: GetAccessPointPolicyStatusRequest = {}  # type: ignore[typeddict-item]
    return out
