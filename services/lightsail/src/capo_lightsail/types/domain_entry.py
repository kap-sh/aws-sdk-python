"""Generated from Smithy shape ``com.amazonaws.lightsail#DomainEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.domain_entry_options
    import capo_lightsail.types.domain_entry_type
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.string


class DomainEntry(TypedDict, closed=True):
    id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the domain recordset entry.</p>"""
    name: NotRequired["capo_lightsail.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    target: NotRequired["capo_lightsail.types.string.string"]
    """<p>The target IP address (<code>192.0.2.0</code>), or AWS name server (<code>ns-111.awsdns-22.com.</code>).</p> <p>For Lightsail load balancers, the value looks like <code>ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com</code>. For Lightsail distributions, the value looks like <code>exampled1182ne.cloudfront.net</code>. For Lightsail container services, the value looks like <code>container-service-1.example23scljs.us-west-2.cs.amazonlightsail.com</code>. Be sure to also set <code>isAlias</code> to <code>true</code> when setting up an A record for a Lightsail load balancer, distribution, or container service.</p>"""
    is_alias: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>When <code>true</code>, specifies whether the domain entry is an alias used by the Lightsail load balancer, Lightsail container service, Lightsail content delivery network (CDN) distribution, or another Amazon Web Services resource. You can include an alias (A type) record in your request, which points to the DNS name of a load balancer, container service, CDN distribution, or other Amazon Web Services resource and routes traffic to that resource.</p>"""
    type: NotRequired["capo_lightsail.types.domain_entry_type.DomainEntryType"]
    """<p>The type of domain entry, such as address for IPv4 (A), address for IPv6 (AAAA), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).</p> <p>The following domain entry types can be used:</p> <ul> <li> <p> <code>A</code> </p> </li> <li> <p> <code>AAAA</code> </p> </li> <li> <p> <code>CNAME</code> </p> </li> <li> <p> <code>MX</code> </p> </li> <li> <p> <code>NS</code> </p> </li> <li> <p> <code>SOA</code> </p> </li> <li> <p> <code>SRV</code> </p> </li> <li> <p> <code>TXT</code> </p> </li> </ul>"""
    options: NotRequired["capo_lightsail.types.domain_entry_options.DomainEntryOptions"]
    """<p>(Discontinued) The options for the domain entry.</p> <note> <p>In releases prior to November 29, 2017, this parameter was not included in the API response. It is now discontinued.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainEntry) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "target" in value:
        out["target"] = value["target"]
    if "is_alias" in value:
        out["isAlias"] = value["is_alias"]
    if "type" in value:
        out["type"] = value["type"]
    if "options" in value:
        import capo_lightsail.types.domain_entry_options

        out["options"] = (
            capo_lightsail.types.domain_entry_options.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainEntry:
    out: DomainEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "target" in data:
        out["target"] = data["target"]
    if "isAlias" in data:
        out["is_alias"] = data["isAlias"]
    if "type" in data:
        out["type"] = data["type"]
    if "options" in data:
        import capo_lightsail.types.domain_entry_options

        out["options"] = (
            capo_lightsail.types.domain_entry_options.deserialize_aws_json_1_1(
                data["options"]
            )
        )
    return out
