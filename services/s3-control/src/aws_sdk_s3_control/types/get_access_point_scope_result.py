"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointScopeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.scope


class GetAccessPointScopeResult(TypedDict):
    scope: NotRequired["aws_sdk_s3_control.types.scope.Scope"]
    """<p>The contents of the access point scope.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetAccessPointScopeResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "scope" in value:
        import aws_sdk_s3_control.types.scope

        aws_sdk_s3_control.types.scope.serialize_xml(value["scope"], el, "Scope")


def deserialize_xml(el: Element) -> GetAccessPointScopeResult:
    out: GetAccessPointScopeResult = {}  # type: ignore[typeddict-item]
    child_scope = el.find("Scope")
    if child_scope is not None:
        import aws_sdk_s3_control.types.scope

        out["scope"] = aws_sdk_s3_control.types.scope.deserialize_xml(child_scope)
    return out
