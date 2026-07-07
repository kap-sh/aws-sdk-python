"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_point_name
    import aws_sdk_s3_control.types.account_id


class GetAccessPointScopeRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that owns the access point with the scope that you want to retrieve. </p>"""
    name: "aws_sdk_s3_control.types.access_point_name.AccessPointName"
    """<p>The name of the access point with the scope you want to retrieve.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetAccessPointScopeRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAccessPointScopeRequest:
    out: GetAccessPointScopeRequest = {}  # type: ignore[typeddict-item]
    return out
