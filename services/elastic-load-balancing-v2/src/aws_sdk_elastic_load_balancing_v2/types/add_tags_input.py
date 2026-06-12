"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.resource_arns
    import aws_sdk_elastic_load_balancing_v2.types.tag_list


class AddTagsInput(TypedDict):
    resource_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["aws_sdk_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.resource_arns

        aws_sdk_elastic_load_balancing_v2.types.resource_arns.serialize_query(
            value["resource_arns"], pairs, f"{prefix}.ResourceArns"
        )
    if "tags" in value:
        import aws_sdk_elastic_load_balancing_v2.types.tag_list

        aws_sdk_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    child_resource_arns = el.find("ResourceArns")
    if child_resource_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.resource_arns

        out["resource_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.resource_arns.deserialize_query(
                child_resource_arns
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_load_balancing_v2.types.tag_list

        out["tags"] = (
            aws_sdk_elastic_load_balancing_v2.types.tag_list.deserialize_query(
                child_tags
            )
        )
    return out
