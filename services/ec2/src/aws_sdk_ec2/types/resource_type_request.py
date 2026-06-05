"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_reference_resource_type
    import aws_sdk_ec2.types.resource_type_option_list


class ResourceTypeRequest(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_ec2.types.image_reference_resource_type.ImageReferenceResourceType"
    ]
    """<p>The resource type.</p>"""
    resource_type_options: NotRequired[
        "aws_sdk_ec2.types.resource_type_option_list.ResourceTypeOptionList"
    ]
    """<p>The options that affect the scope of the response. Valid only when <code>ResourceType</code> is <code>ec2:Instance</code> or <code>ec2:LaunchTemplate</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceTypeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_type" in value:
        import aws_sdk_ec2.types.image_reference_resource_type

        aws_sdk_ec2.types.image_reference_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_type_options" in value:
        import aws_sdk_ec2.types.resource_type_option_list

        aws_sdk_ec2.types.resource_type_option_list.serialize_ec2_query(
            value["resource_type_options"], pairs, f"{prefix}.ResourceTypeOptions"
        )


def deserialize_ec2_query(el: Element) -> ResourceTypeRequest:
    out: ResourceTypeRequest = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.image_reference_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.image_reference_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    if el.find("ResourceTypeOptions") is not None:
        import aws_sdk_ec2.types.resource_type_option_list

        out["resource_type_options"] = (
            aws_sdk_ec2.types.resource_type_option_list.deserialize_ec2_query(
                el, "ResourceTypeOptions"
            )
        )
    return out
