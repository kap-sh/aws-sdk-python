"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchConfigurationNameType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class LaunchConfigurationNameType(TypedDict, closed=True):
    launch_configuration_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the launch configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchConfigurationNameType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_configuration_name" in value:
        pairs.append(
            (
                f"{prefix}.LaunchConfigurationName",
                str(value["launch_configuration_name"]),
            )
        )


def deserialize_query(el: Element) -> LaunchConfigurationNameType:
    out: LaunchConfigurationNameType = {}  # type: ignore[typeddict-item]
    child_launch_configuration_name = el.find("LaunchConfigurationName")
    if child_launch_configuration_name is not None:
        out["launch_configuration_name"] = str(
            child_launch_configuration_name.text or ""
        )
    return out
