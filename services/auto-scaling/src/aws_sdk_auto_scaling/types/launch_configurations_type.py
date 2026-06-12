"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchConfigurationsType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.launch_configurations
    import aws_sdk_auto_scaling.types.xml_string


class LaunchConfigurationsType(TypedDict):
    launch_configurations: NotRequired[
        "aws_sdk_auto_scaling.types.launch_configurations.LaunchConfigurations"
    ]
    """<p>The launch configurations.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchConfigurationsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_configurations" in value:
        import aws_sdk_auto_scaling.types.launch_configurations

        aws_sdk_auto_scaling.types.launch_configurations.serialize_query(
            value["launch_configurations"], pairs, f"{prefix}.LaunchConfigurations"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> LaunchConfigurationsType:
    out: LaunchConfigurationsType = {}  # type: ignore[typeddict-item]
    child_launch_configurations = el.find("LaunchConfigurations")
    if child_launch_configurations is not None:
        import aws_sdk_auto_scaling.types.launch_configurations

        out["launch_configurations"] = (
            aws_sdk_auto_scaling.types.launch_configurations.deserialize_query(
                child_launch_configurations
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
