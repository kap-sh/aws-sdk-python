"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHostedZoneFeaturesResponse``."""

from typing import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class UpdateHostedZoneFeaturesResponse(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateHostedZoneFeaturesResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UpdateHostedZoneFeaturesResponse:
    out: UpdateHostedZoneFeaturesResponse = {}  # type: ignore[typeddict-item]
    return out
