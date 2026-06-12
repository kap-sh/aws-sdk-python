"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneLimit``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.hosted_zone_limit_type
    import aws_sdk_route_53.types.limit_value


class HostedZoneLimit(TypedDict):
    type: "aws_sdk_route_53.types.hosted_zone_limit_type.HostedZoneLimitType"
    """<p>The limit that you requested. Valid values include the following:</p> <ul> <li> <p> <b>MAX_RRSETS_BY_ZONE</b>: The maximum number of records that you can create in the specified hosted zone.</p> </li> <li> <p> <b>MAX_VPCS_ASSOCIATED_BY_ZONE</b>: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.</p> </li> </ul>"""
    value: "aws_sdk_route_53.types.limit_value.LimitValue"
    """<p>The current value for the limit that is specified by <code>Type</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneLimit, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.hosted_zone_limit_type

    aws_sdk_route_53.types.hosted_zone_limit_type.serialize_xml(
        value["type"], el, "Type"
    )
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> HostedZoneLimit:
    out: HostedZoneLimit = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_route_53.types.hosted_zone_limit_type

        out["type"] = aws_sdk_route_53.types.hosted_zone_limit_type.deserialize_xml(
            child_type
        )
    else:
        raise DeserializationError("HostedZoneLimit.type required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    else:
        raise DeserializationError("HostedZoneLimit.value required")
    return out
