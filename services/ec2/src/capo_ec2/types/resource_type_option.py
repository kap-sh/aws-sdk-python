"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_reference_option_name
    import capo_ec2.types.resource_type_option_values_list


class ResourceTypeOption(TypedDict, closed=True):
    option_name: NotRequired[
        "capo_ec2.types.image_reference_option_name.ImageReferenceOptionName"
    ]
    """<p>The name of the option.</p> <ul> <li> <p>For <code>ec2:Instance</code>:</p> <p>Specify <code>state-name</code> - The current state of the EC2 instance.</p> </li> <li> <p>For <code>ec2:LaunchTemplate</code>:</p> <p>Specify <code>version-depth</code> - The number of launch template versions to check, starting from the most recent version.</p> </li> </ul>"""
    option_values: NotRequired[
        "capo_ec2.types.resource_type_option_values_list.ResourceTypeOptionValuesList"
    ]
    """<p>A value for the specified option.</p> <ul> <li> <p>For <code>state-name</code>:</p> <ul> <li> <p>Valid values: <code>pending</code> | <code>running</code> | <code>shutting-down</code> | <code>terminated</code> | <code>stopping</code> | <code>stopped</code> </p> </li> <li> <p>Default: All states</p> </li> </ul> </li> <li> <p>For <code>version-depth</code>:</p> <ul> <li> <p>Valid values: Integers between <code>1</code> and <code>10000</code> </p> </li> <li> <p>Default: <code>10</code> </p> </li> </ul> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceTypeOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_name" in value:
        import capo_ec2.types.image_reference_option_name

        capo_ec2.types.image_reference_option_name.serialize_ec2_query(
            value["option_name"], pairs, f"{prefix}.OptionName"
        )
    if "option_values" in value:
        import capo_ec2.types.resource_type_option_values_list

        capo_ec2.types.resource_type_option_values_list.serialize_ec2_query(
            value["option_values"], pairs, f"{prefix}.OptionValues"
        )


def deserialize_ec2_query(el: Element) -> ResourceTypeOption:
    out: ResourceTypeOption = {}  # type: ignore[typeddict-item]
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        import capo_ec2.types.image_reference_option_name

        out["option_name"] = (
            capo_ec2.types.image_reference_option_name.deserialize_ec2_query(
                child_option_name
            )
        )
    if el.find("OptionValues") is not None:
        import capo_ec2.types.resource_type_option_values_list

        out["option_values"] = (
            capo_ec2.types.resource_type_option_values_list.deserialize_ec2_query(
                el, "OptionValues"
            )
        )
    return out
