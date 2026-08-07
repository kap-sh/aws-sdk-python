"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentResourcesDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.load_balancer_description


class EnvironmentResourcesDescription(TypedDict, closed=True):
    load_balancer: NotRequired[
        "capo_elastic_beanstalk.types.load_balancer_description.LoadBalancerDescription"
    ]
    """<p>Describes the LoadBalancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentResourcesDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer" in value:
        import capo_elastic_beanstalk.types.load_balancer_description

        capo_elastic_beanstalk.types.load_balancer_description.serialize_query(
            value["load_balancer"], pairs, f"{key_prefix}LoadBalancer"
        )


def deserialize_query(el: Element) -> EnvironmentResourcesDescription:
    out: EnvironmentResourcesDescription = {}  # type: ignore[typeddict-item]
    child_load_balancer = el.find("LoadBalancer")
    if child_load_balancer is not None:
        import capo_elastic_beanstalk.types.load_balancer_description

        out["load_balancer"] = (
            capo_elastic_beanstalk.types.load_balancer_description.deserialize_query(
                child_load_balancer
            )
        )
    return out
