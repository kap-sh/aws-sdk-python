"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentResourcesDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.load_balancer_description


class EnvironmentResourcesDescription(TypedDict):
    load_balancer: NotRequired[
        "aws_sdk_elastic_beanstalk.types.load_balancer_description.LoadBalancerDescription"
    ]
    """<p>Describes the LoadBalancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentResourcesDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer" in value:
        import aws_sdk_elastic_beanstalk.types.load_balancer_description

        aws_sdk_elastic_beanstalk.types.load_balancer_description.serialize_query(
            value["load_balancer"], pairs, f"{prefix}.LoadBalancer"
        )


def deserialize_query(el: Element) -> EnvironmentResourcesDescription:
    out: EnvironmentResourcesDescription = {}  # type: ignore[typeddict-item]
    child_load_balancer = el.find("LoadBalancer")
    if child_load_balancer is not None:
        import aws_sdk_elastic_beanstalk.types.load_balancer_description

        out["load_balancer"] = (
            aws_sdk_elastic_beanstalk.types.load_balancer_description.deserialize_query(
                child_load_balancer
            )
        )
    return out
