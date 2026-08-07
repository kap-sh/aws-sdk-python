"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TagDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.resource_arn
    import capo_elastic_load_balancing_v2.types.tag_list


class TagDescription(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["capo_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>Information about the tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    if "tags" in value:
        import capo_elastic_load_balancing_v2.types.tag_list

        capo_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> TagDescription:
    out: TagDescription = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing_v2.types.tag_list

        out["tags"] = capo_elastic_load_balancing_v2.types.tag_list.deserialize_query(
            child_tags
        )
    return out
