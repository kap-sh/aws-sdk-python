"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.resource_arns
    import capo_elastic_load_balancing_v2.types.tag_keys


class RemoveTagsInput(TypedDict, closed=True):
    resource_arns: NotRequired[
        "capo_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: NotRequired["capo_elastic_load_balancing_v2.types.tag_keys.TagKeys"]
    """<p>The tag keys for the tags to remove.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arns" in value:
        import capo_elastic_load_balancing_v2.types.resource_arns

        capo_elastic_load_balancing_v2.types.resource_arns.serialize_query(
            value["resource_arns"], pairs, f"{key_prefix}ResourceArns"
        )
    if "tag_keys" in value:
        import capo_elastic_load_balancing_v2.types.tag_keys

        capo_elastic_load_balancing_v2.types.tag_keys.serialize_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeys"
        )


def deserialize_query(el: Element) -> RemoveTagsInput:
    out: RemoveTagsInput = {}  # type: ignore[typeddict-item]
    child_resource_arns = el.find("ResourceArns")
    if child_resource_arns is not None:
        import capo_elastic_load_balancing_v2.types.resource_arns

        out["resource_arns"] = (
            capo_elastic_load_balancing_v2.types.resource_arns.deserialize_query(
                child_resource_arns
            )
        )
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_elastic_load_balancing_v2.types.tag_keys

        out["tag_keys"] = (
            capo_elastic_load_balancing_v2.types.tag_keys.deserialize_query(
                child_tag_keys
            )
        )
    return out
