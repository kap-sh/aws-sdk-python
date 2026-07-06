"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.tag_descriptions


class DescribeTagsOutput(TypedDict, closed=True):
    tag_descriptions: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.tag_descriptions.TagDescriptions"
    ]
    """<p>Information about the tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTagsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tag_descriptions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.tag_descriptions

        aws_sdk_elastic_load_balancing_v2.types.tag_descriptions.serialize_query(
            value["tag_descriptions"], pairs, f"{prefix}.TagDescriptions"
        )


def deserialize_query(el: Element) -> DescribeTagsOutput:
    out: DescribeTagsOutput = {}  # type: ignore[typeddict-item]
    child_tag_descriptions = el.find("TagDescriptions")
    if child_tag_descriptions is not None:
        import aws_sdk_elastic_load_balancing_v2.types.tag_descriptions

        out["tag_descriptions"] = (
            aws_sdk_elastic_load_balancing_v2.types.tag_descriptions.deserialize_query(
                child_tag_descriptions
            )
        )
    return out
