"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.resource_arns
    import aws_sdk_elastic_load_balancing_v2.types.tag_keys


class RemoveTagsInput(TypedDict):
    resource_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: NotRequired["aws_sdk_elastic_load_balancing_v2.types.tag_keys.TagKeys"]
    """<p>The tag keys for the tags to remove.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.resource_arns

        aws_sdk_elastic_load_balancing_v2.types.resource_arns.serialize_query(
            value["resource_arns"], pairs, f"{prefix}.ResourceArns"
        )
    if "tag_keys" in value:
        import aws_sdk_elastic_load_balancing_v2.types.tag_keys

        aws_sdk_elastic_load_balancing_v2.types.tag_keys.serialize_query(
            value["tag_keys"], pairs, f"{prefix}.TagKeys"
        )


def deserialize_query(el: Element) -> RemoveTagsInput:
    out: RemoveTagsInput = {}  # type: ignore[typeddict-item]
    child_resource_arns = el.find("ResourceArns")
    if child_resource_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.resource_arns

        out["resource_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.resource_arns.deserialize_query(
                child_resource_arns
            )
        )
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_elastic_load_balancing_v2.types.tag_keys

        out["tag_keys"] = (
            aws_sdk_elastic_load_balancing_v2.types.tag_keys.deserialize_query(
                child_tag_keys
            )
        )
    return out
