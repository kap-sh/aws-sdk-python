"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_reference_resource_type
    import capo_ec2.types.resource_type_option_list


class ResourceTypeRequest(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_ec2.types.image_reference_resource_type.ImageReferenceResourceType"
    ]
    """<p>The resource type.</p>"""
    resource_type_options: NotRequired[
        "capo_ec2.types.resource_type_option_list.ResourceTypeOptionList"
    ]
    """<p>The options that affect the scope of the response. Valid only when <code>ResourceType</code> is <code>ec2:Instance</code> or <code>ec2:LaunchTemplate</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceTypeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        import capo_ec2.types.image_reference_resource_type

        capo_ec2.types.image_reference_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_type_options" in value:
        import capo_ec2.types.resource_type_option_list

        capo_ec2.types.resource_type_option_list.serialize_ec2_query(
            value["resource_type_options"], pairs, f"{key_prefix}ResourceTypeOptions"
        )


def deserialize_ec2_query(el: Element) -> ResourceTypeRequest:
    out: ResourceTypeRequest = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.image_reference_resource_type

        out["resource_type"] = (
            capo_ec2.types.image_reference_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    if el.find("ResourceTypeOptions") is not None:
        import capo_ec2.types.resource_type_option_list

        out["resource_type_options"] = (
            capo_ec2.types.resource_type_option_list.deserialize_ec2_query(
                el, "ResourceTypeOptions"
            )
        )
    return out
