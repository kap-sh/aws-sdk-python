"""Generated from Smithy shape ``com.amazonaws.route53#GetCheckerIpRangesRequest``."""

from typing import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class GetCheckerIpRangesRequest(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: GetCheckerIpRangesRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetCheckerIpRangesRequest:
    out: GetCheckerIpRangesRequest = {}  # type: ignore[typeddict-item]
    return out
