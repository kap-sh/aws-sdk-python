"""Generated from Smithy shape ``com.amazonaws.route53#ReusableDelegationSetLimit``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.limit_value
    import aws_sdk_route_53.types.reusable_delegation_set_limit_type


class ReusableDelegationSetLimit(TypedDict):
    type: "aws_sdk_route_53.types.reusable_delegation_set_limit_type.ReusableDelegationSetLimitType"
    """<p>The limit that you requested: <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code>, the maximum number of hosted zones that you can associate with the specified reusable delegation set.</p>"""
    value: "aws_sdk_route_53.types.limit_value.LimitValue"
    """<p>The current value for the <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code> limit.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReusableDelegationSetLimit, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.reusable_delegation_set_limit_type

    aws_sdk_route_53.types.reusable_delegation_set_limit_type.serialize_xml(
        value["type"], el, "Type"
    )
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> ReusableDelegationSetLimit:
    out: ReusableDelegationSetLimit = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_route_53.types.reusable_delegation_set_limit_type

        out["type"] = (
            aws_sdk_route_53.types.reusable_delegation_set_limit_type.deserialize_xml(
                child_type
            )
        )
    else:
        raise DeserializationError("ReusableDelegationSetLimit.type required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    else:
        raise DeserializationError("ReusableDelegationSetLimit.value required")
    return out
