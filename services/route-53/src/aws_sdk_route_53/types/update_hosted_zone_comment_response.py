"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHostedZoneCommentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.hosted_zone


class UpdateHostedZoneCommentResponse(TypedDict):
    hosted_zone: "aws_sdk_route_53.types.hosted_zone.HostedZone"
    """<p>A complex type that contains the response to the <code>UpdateHostedZoneComment</code> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateHostedZoneCommentResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.hosted_zone

    aws_sdk_route_53.types.hosted_zone.serialize_xml(
        value["hosted_zone"], el, "HostedZone"
    )


def deserialize_xml(el: Element) -> UpdateHostedZoneCommentResponse:
    out: UpdateHostedZoneCommentResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone = el.find("HostedZone")
    if child_hosted_zone is not None:
        import aws_sdk_route_53.types.hosted_zone

        out["hosted_zone"] = aws_sdk_route_53.types.hosted_zone.deserialize_xml(
            child_hosted_zone
        )
    else:
        raise DeserializationError(
            "UpdateHostedZoneCommentResponse.hosted_zone required"
        )
    return out
