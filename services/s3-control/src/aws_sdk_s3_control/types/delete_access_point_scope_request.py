"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteAccessPointScopeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_point_name
    import aws_sdk_s3_control.types.account_id


class DeleteAccessPointScopeRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that owns the access point with the scope that you want to delete. </p>"""
    name: "aws_sdk_s3_control.types.access_point_name.AccessPointName"
    """<p> The name of the access point with the scope that you want to delete. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteAccessPointScopeRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteAccessPointScopeRequest:
    out: DeleteAccessPointScopeRequest = {}  # type: ignore[typeddict-item]
    return out
