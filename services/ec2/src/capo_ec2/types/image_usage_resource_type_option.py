"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_resource_type_option_values_list
    import capo_ec2.types.string


class ImageUsageResourceTypeOption(TypedDict, closed=True):
    option_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the option.</p>"""
    option_values: NotRequired[
        "capo_ec2.types.image_usage_resource_type_option_values_list.ImageUsageResourceTypeOptionValuesList"
    ]
    """<p>The number of launch template versions to check.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageResourceTypeOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_name" in value:
        pairs.append((f"{key_prefix}OptionName", str(value["option_name"])))
    if "option_values" in value:
        import capo_ec2.types.image_usage_resource_type_option_values_list

        capo_ec2.types.image_usage_resource_type_option_values_list.serialize_ec2_query(
            value["option_values"], pairs, f"{key_prefix}OptionValueSet"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageResourceTypeOption:
    out: ImageUsageResourceTypeOption = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("optionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    child_option_values = el.find("optionValueSet")
    if child_option_values is not None:
        import capo_ec2.types.image_usage_resource_type_option_values_list

        out["option_values"] = (
            capo_ec2.types.image_usage_resource_type_option_values_list.deserialize_ec2_query(
                child_option_values
            )
        )
    return out
