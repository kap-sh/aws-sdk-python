"""Generated from Smithy shape ``com.amazonaws.s3control#PutAccessPointScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_point_name
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.scope


class PutAccessPointScopeRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that owns the access point with scope that you want to create or replace. </p>"""
    name: "aws_sdk_s3_control.types.access_point_name.AccessPointName"
    """<p>The name of the access point with the scope that you want to create or replace.</p>"""
    scope: "aws_sdk_s3_control.types.scope.Scope"
    """<p>Object prefixes, API operations, or a combination of both.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutAccessPointScopeRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.scope

    aws_sdk_s3_control.types.scope.serialize_xml(value["scope"], el, "Scope")


def deserialize_xml(el: Element) -> PutAccessPointScopeRequest:
    out: PutAccessPointScopeRequest = {}  # type: ignore[typeddict-item]
    child_scope = el.find("Scope")
    if child_scope is not None:
        import aws_sdk_s3_control.types.scope

        out["scope"] = aws_sdk_s3_control.types.scope.deserialize_xml(child_scope)
    else:
        raise DeserializationError("PutAccessPointScopeRequest.scope required")
    return out
