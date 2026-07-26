"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeAccountLimitsAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.max_number_of_auto_scaling_groups
    import capo_auto_scaling.types.max_number_of_launch_configurations
    import capo_auto_scaling.types.number_of_auto_scaling_groups
    import capo_auto_scaling.types.number_of_launch_configurations


class DescribeAccountLimitsAnswer(TypedDict, closed=True):
    max_number_of_auto_scaling_groups: NotRequired[
        "capo_auto_scaling.types.max_number_of_auto_scaling_groups.MaxNumberOfAutoScalingGroups"
    ]
    """<p>The maximum number of groups allowed for your account. The default is 200 groups per Region.</p>"""
    max_number_of_launch_configurations: NotRequired[
        "capo_auto_scaling.types.max_number_of_launch_configurations.MaxNumberOfLaunchConfigurations"
    ]
    """<p>The maximum number of launch configurations allowed for your account. The default is 200 launch configurations per Region.</p>"""
    number_of_auto_scaling_groups: NotRequired[
        "capo_auto_scaling.types.number_of_auto_scaling_groups.NumberOfAutoScalingGroups"
    ]
    """<p>The current number of groups for your account.</p>"""
    number_of_launch_configurations: NotRequired[
        "capo_auto_scaling.types.number_of_launch_configurations.NumberOfLaunchConfigurations"
    ]
    """<p>The current number of launch configurations for your account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountLimitsAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "max_number_of_auto_scaling_groups" in value:
        pairs.append(
            (
                f"{prefix}.MaxNumberOfAutoScalingGroups",
                str(value["max_number_of_auto_scaling_groups"]),
            )
        )
    if "max_number_of_launch_configurations" in value:
        pairs.append(
            (
                f"{prefix}.MaxNumberOfLaunchConfigurations",
                str(value["max_number_of_launch_configurations"]),
            )
        )
    if "number_of_auto_scaling_groups" in value:
        pairs.append(
            (
                f"{prefix}.NumberOfAutoScalingGroups",
                str(value["number_of_auto_scaling_groups"]),
            )
        )
    if "number_of_launch_configurations" in value:
        pairs.append(
            (
                f"{prefix}.NumberOfLaunchConfigurations",
                str(value["number_of_launch_configurations"]),
            )
        )


def deserialize_query(el: Element) -> DescribeAccountLimitsAnswer:
    out: DescribeAccountLimitsAnswer = {}  # type: ignore[typeddict-item]
    child_max_number_of_auto_scaling_groups = el.find("MaxNumberOfAutoScalingGroups")
    if child_max_number_of_auto_scaling_groups is not None:
        out["max_number_of_auto_scaling_groups"] = int(
            child_max_number_of_auto_scaling_groups.text or ""
        )
    child_max_number_of_launch_configurations = el.find(
        "MaxNumberOfLaunchConfigurations"
    )
    if child_max_number_of_launch_configurations is not None:
        out["max_number_of_launch_configurations"] = int(
            child_max_number_of_launch_configurations.text or ""
        )
    child_number_of_auto_scaling_groups = el.find("NumberOfAutoScalingGroups")
    if child_number_of_auto_scaling_groups is not None:
        out["number_of_auto_scaling_groups"] = int(
            child_number_of_auto_scaling_groups.text or ""
        )
    child_number_of_launch_configurations = el.find("NumberOfLaunchConfigurations")
    if child_number_of_launch_configurations is not None:
        out["number_of_launch_configurations"] = int(
            child_number_of_launch_configurations.text or ""
        )
    return out
