"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LoadBalancerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.load_balancer_listeners_description
    import capo_elastic_beanstalk.types.string


class LoadBalancerDescription(TypedDict, closed=True):
    load_balancer_name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the LoadBalancer.</p>"""
    domain: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The domain name of the LoadBalancer.</p>"""
    listeners: NotRequired[
        "capo_elastic_beanstalk.types.load_balancer_listeners_description.LoadBalancerListenersDescription"
    ]
    """<p>A list of Listeners used by the LoadBalancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_name" in value:
        pairs.append(
            (f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"]))
        )
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "listeners" in value:
        import capo_elastic_beanstalk.types.load_balancer_listeners_description

        capo_elastic_beanstalk.types.load_balancer_listeners_description.serialize_query(
            value["listeners"], pairs, f"{key_prefix}Listeners"
        )


def deserialize_query(el: Element) -> LoadBalancerDescription:
    out: LoadBalancerDescription = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import capo_elastic_beanstalk.types.load_balancer_listeners_description

        out["listeners"] = (
            capo_elastic_beanstalk.types.load_balancer_listeners_description.deserialize_query(
                child_listeners
            )
        )
    return out
