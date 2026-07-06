"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_option_values_list
    import aws_sdk_ec2.types.string


class ImageUsageResourceTypeOption(TypedDict, closed=True):
    option_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the option.</p>"""
    option_values: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_option_values_list.ImageUsageResourceTypeOptionValuesList"
    ]
    """<p>The number of launch template versions to check.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageResourceTypeOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_name" in value:
        pairs.append((f"{prefix}.OptionName", str(value["option_name"])))
    if "option_values" in value:
        import aws_sdk_ec2.types.image_usage_resource_type_option_values_list

        aws_sdk_ec2.types.image_usage_resource_type_option_values_list.serialize_ec2_query(
            value["option_values"], pairs, f"{prefix}.OptionValueSet"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageResourceTypeOption:
    out: ImageUsageResourceTypeOption = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    if el.find("OptionValueSet") is not None:
        import aws_sdk_ec2.types.image_usage_resource_type_option_values_list

        out["option_values"] = (
            aws_sdk_ec2.types.image_usage_resource_type_option_values_list.deserialize_ec2_query(
                el, "OptionValueSet"
            )
        )
    return out
