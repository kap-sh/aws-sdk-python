"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.resource_arns
    import capo_elastic_load_balancing_v2.types.tag_list


class AddTagsInput(TypedDict, closed=True):
    resource_arns: NotRequired[
        "capo_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["capo_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arns" in value:
        import capo_elastic_load_balancing_v2.types.resource_arns

        capo_elastic_load_balancing_v2.types.resource_arns.serialize_query(
            value["resource_arns"], pairs, f"{prefix}.ResourceArns"
        )
    if "tags" in value:
        import capo_elastic_load_balancing_v2.types.tag_list

        capo_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    child_resource_arns = el.find("ResourceArns")
    if child_resource_arns is not None:
        import capo_elastic_load_balancing_v2.types.resource_arns

        out["resource_arns"] = (
            capo_elastic_load_balancing_v2.types.resource_arns.deserialize_query(
                child_resource_arns
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing_v2.types.tag_list

        out["tags"] = capo_elastic_load_balancing_v2.types.tag_list.deserialize_query(
            child_tags
        )
    return out
