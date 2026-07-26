"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateGlobalResolverInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.global_resolver_ip_address_type
    import capo_route53globalresolver.types.region
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class UpdateGlobalResolverInput(TypedDict, closed=True):
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Global Resolver.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the Global Resolver.</p>"""
    observability_region: NotRequired["capo_route53globalresolver.types.region.Region"]
    """<p>The Amazon Web Services Regions in which the users' Global Resolver query resolution logs will be propagated.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the Global Resolver.</p>"""
    ip_address_type: NotRequired[
        "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type for the Global Resolver. Valid values are IPV4 or DUAL_STACK for both IPv4 and IPv6 support.</p>"""
    regions: NotRequired["capo_route53globalresolver.types.regions.Regions"]
    """<p>The list of Amazon Web Services Regions where the Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalResolverInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "observability_region" in value:
        out["observabilityRegion"] = value["observability_region"]
    if "description" in value:
        out["description"] = value["description"]
    if "ip_address_type" in value:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    if "regions" in value:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGlobalResolverInput:
    out: UpdateGlobalResolverInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "observabilityRegion" in data:
        out["observability_region"] = data["observabilityRegion"]
    if "description" in data:
        out["description"] = data["description"]
    if "ipAddressType" in data:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if "regions" in data:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    return out
