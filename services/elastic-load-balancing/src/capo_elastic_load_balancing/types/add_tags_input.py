"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AddTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.load_balancer_names
    import capo_elastic_load_balancing.types.tag_list


class AddTagsInput(TypedDict, closed=True):
    load_balancer_names: (
        "capo_elastic_load_balancing.types.load_balancer_names.LoadBalancerNames"
    )
    """<p>The name of the load balancer. You can specify one load balancer only.</p>"""
    tags: "capo_elastic_load_balancing.types.tag_list.TagList"
    """<p>The tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_elastic_load_balancing.types.load_balancer_names

    capo_elastic_load_balancing.types.load_balancer_names.serialize_query(
        value["load_balancer_names"], pairs, f"{key_prefix}LoadBalancerNames"
    )
    import capo_elastic_load_balancing.types.tag_list

    capo_elastic_load_balancing.types.tag_list.serialize_query(
        value["tags"], pairs, f"{key_prefix}Tags"
    )


def deserialize_query(el: Element) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_names = el.find("LoadBalancerNames")
    if child_load_balancer_names is not None:
        import capo_elastic_load_balancing.types.load_balancer_names

        out["load_balancer_names"] = (
            capo_elastic_load_balancing.types.load_balancer_names.deserialize_query(
                child_load_balancer_names
            )
        )
    else:
        raise DeserializationError("AddTagsInput.load_balancer_names required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing.types.tag_list

        out["tags"] = capo_elastic_load_balancing.types.tag_list.deserialize_query(
            child_tags
        )
    else:
        raise DeserializationError("AddTagsInput.tags required")
    return out
