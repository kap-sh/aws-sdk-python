"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SslPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.ciphers
    import capo_elastic_load_balancing_v2.types.list_of_string
    import capo_elastic_load_balancing_v2.types.ssl_policy_name
    import capo_elastic_load_balancing_v2.types.ssl_protocols


class SslPolicy(TypedDict, closed=True):
    ssl_protocols: NotRequired[
        "capo_elastic_load_balancing_v2.types.ssl_protocols.SslProtocols"
    ]
    """<p>The protocols.</p>"""
    ciphers: NotRequired["capo_elastic_load_balancing_v2.types.ciphers.Ciphers"]
    """<p>The ciphers.</p>"""
    name: NotRequired[
        "capo_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
    ]
    """<p>The name of the policy.</p>"""
    supported_load_balancer_types: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p> The supported load balancers. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SslPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ssl_protocols" in value:
        import capo_elastic_load_balancing_v2.types.ssl_protocols

        capo_elastic_load_balancing_v2.types.ssl_protocols.serialize_query(
            value["ssl_protocols"], pairs, f"{prefix}.SslProtocols"
        )
    if "ciphers" in value:
        import capo_elastic_load_balancing_v2.types.ciphers

        capo_elastic_load_balancing_v2.types.ciphers.serialize_query(
            value["ciphers"], pairs, f"{prefix}.Ciphers"
        )
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "supported_load_balancer_types" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["supported_load_balancer_types"],
            pairs,
            f"{prefix}.SupportedLoadBalancerTypes",
        )


def deserialize_query(el: Element) -> SslPolicy:
    out: SslPolicy = {}  # type: ignore[typeddict-item]
    child_ssl_protocols = el.find("SslProtocols")
    if child_ssl_protocols is not None:
        import capo_elastic_load_balancing_v2.types.ssl_protocols

        out["ssl_protocols"] = (
            capo_elastic_load_balancing_v2.types.ssl_protocols.deserialize_query(
                child_ssl_protocols
            )
        )
    child_ciphers = el.find("Ciphers")
    if child_ciphers is not None:
        import capo_elastic_load_balancing_v2.types.ciphers

        out["ciphers"] = capo_elastic_load_balancing_v2.types.ciphers.deserialize_query(
            child_ciphers
        )
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_supported_load_balancer_types = el.find("SupportedLoadBalancerTypes")
    if child_supported_load_balancer_types is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["supported_load_balancer_types"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_supported_load_balancer_types
            )
        )
    return out
