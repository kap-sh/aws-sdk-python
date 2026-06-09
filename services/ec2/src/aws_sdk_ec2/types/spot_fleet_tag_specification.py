"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetTagSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type
    import aws_sdk_ec2.types.tag_list


class SpotFleetTagSpecification(TypedDict):
    resource_type: NotRequired["aws_sdk_ec2.types.resource_type.ResourceType"]
    """<p>The type of resource. Currently, the only resource type that is supported is <code>instance</code>. To tag the Spot Fleet request on creation, use the <code>TagSpecifications</code> parameter in <code> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html\">SpotFleetRequestConfigData</a> </code>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetTagSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_type" in value:
        import aws_sdk_ec2.types.resource_type

        aws_sdk_ec2.types.resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.Tag"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetTagSpecification:
    out: SpotFleetTagSpecification = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.resource_type

        out["resource_type"] = aws_sdk_ec2.types.resource_type.deserialize_ec2_query(
            child_resource_type
        )
    if el.find("Tag") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "Tag")
    return out
