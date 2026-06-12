"""Generated from Smithy shape ``com.amazonaws.route53#LinkedService``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_description
    import aws_sdk_route_53.types.service_principal


class LinkedService(TypedDict):
    service_principal: NotRequired[
        "aws_sdk_route_53.types.service_principal.ServicePrincipal"
    ]
    """<p>If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. </p>"""
    description: NotRequired[
        "aws_sdk_route_53.types.resource_description.ResourceDescription"
    ]
    """<p>If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: LinkedService, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "service_principal" in value:
        SubElement(el, "ServicePrincipal").text = str(value["service_principal"])
    if "description" in value:
        SubElement(el, "Description").text = str(value["description"])


def deserialize_xml(el: Element) -> LinkedService:
    out: LinkedService = {}  # type: ignore[typeddict-item]
    child_service_principal = el.find("ServicePrincipal")
    if child_service_principal is not None:
        out["service_principal"] = str(child_service_principal.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
