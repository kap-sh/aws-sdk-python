"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.aws_account_id
    import aws_sdk_route_53.types.hosted_zone_owning_service


class HostedZoneOwner(TypedDict, closed=True):
    owning_account: NotRequired["aws_sdk_route_53.types.aws_account_id.AWSAccountID"]
    """<p>If the hosted zone was created by an Amazon Web Services account, or was created by an Amazon Web Services service that creates hosted zones using the current account, <code>OwningAccount</code> contains the account ID of that account. For example, when you use Cloud Map to create a hosted zone, Cloud Map creates the hosted zone using the current Amazon Web Services account. </p>"""
    owning_service: NotRequired[
        "aws_sdk_route_53.types.hosted_zone_owning_service.HostedZoneOwningService"
    ]
    """<p>If an Amazon Web Services service uses its own account to create a hosted zone and associate the specified VPC with that hosted zone, <code>OwningService</code> contains an abbreviation that identifies the service. For example, if Amazon Elastic File System (Amazon EFS) created a hosted zone and associated a VPC with the hosted zone, the value of <code>OwningService</code> is <code>efs.amazonaws.com</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneOwner, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "owning_account" in value:
        SubElement(el, "OwningAccount").text = str(value["owning_account"])
    if "owning_service" in value:
        SubElement(el, "OwningService").text = str(value["owning_service"])


def deserialize_xml(el: Element) -> HostedZoneOwner:
    out: HostedZoneOwner = {}  # type: ignore[typeddict-item]
    child_owning_account = el.find("OwningAccount")
    if child_owning_account is not None:
        out["owning_account"] = str(child_owning_account.text or "")
    child_owning_service = el.find("OwningService")
    if child_owning_service is not None:
        out["owning_service"] = str(child_owning_service.text or "")
    return out
