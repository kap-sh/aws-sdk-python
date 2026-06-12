"""Generated from Smithy shape ``com.amazonaws.route53#GetReusableDelegationSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.delegation_set


class GetReusableDelegationSetResponse(TypedDict):
    delegation_set: "aws_sdk_route_53.types.delegation_set.DelegationSet"
    """<p>A complex type that contains information about the reusable delegation set.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetReusableDelegationSetResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.delegation_set

    aws_sdk_route_53.types.delegation_set.serialize_xml(
        value["delegation_set"], el, "DelegationSet"
    )


def deserialize_xml(el: Element) -> GetReusableDelegationSetResponse:
    out: GetReusableDelegationSetResponse = {}  # type: ignore[typeddict-item]
    child_delegation_set = el.find("DelegationSet")
    if child_delegation_set is not None:
        import aws_sdk_route_53.types.delegation_set

        out["delegation_set"] = aws_sdk_route_53.types.delegation_set.deserialize_xml(
            child_delegation_set
        )
    else:
        raise DeserializationError(
            "GetReusableDelegationSetResponse.delegation_set required"
        )
    return out
