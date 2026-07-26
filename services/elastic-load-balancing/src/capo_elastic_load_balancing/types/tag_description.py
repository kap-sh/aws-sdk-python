"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#TagDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.tag_list


class TagDescription(TypedDict, closed=True):
    load_balancer_name: NotRequired[
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    ]
    """<p>The name of the load balancer.</p>"""
    tags: NotRequired["capo_elastic_load_balancing.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_name" in value:
        pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    if "tags" in value:
        import capo_elastic_load_balancing.types.tag_list

        capo_elastic_load_balancing.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> TagDescription:
    out: TagDescription = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing.types.tag_list

        out["tags"] = capo_elastic_load_balancing.types.tag_list.deserialize_query(
            child_tags
        )
    return out
