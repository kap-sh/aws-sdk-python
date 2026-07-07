"""Generated from Smithy shape ``com.amazonaws.autoscaling#StartInstanceRefreshType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.desired_configuration
    import aws_sdk_auto_scaling.types.refresh_preferences
    import aws_sdk_auto_scaling.types.refresh_strategy
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class StartInstanceRefreshType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    strategy: NotRequired["aws_sdk_auto_scaling.types.refresh_strategy.RefreshStrategy"]
    """<p>The strategy to use for the instance refresh. The default value is <code>Rolling</code>.</p>"""
    desired_configuration: NotRequired[
        "aws_sdk_auto_scaling.types.desired_configuration.DesiredConfiguration"
    ]
    """<p>The desired configuration. For example, the desired configuration can specify a new launch template or a new version of the current launch template.</p> <p>Once the instance refresh succeeds, Amazon EC2 Auto Scaling updates the settings of the Auto Scaling group to reflect the new desired configuration. </p> <note> <p>When you specify a new launch template or a new version of the current launch template for your desired configuration, consider enabling the <code>SkipMatching</code> property in preferences. If it's enabled, Amazon EC2 Auto Scaling skips replacing instances that already use the specified launch template and instance types. This can help you reduce the number of replacements that are required to apply updates. </p> </note>"""
    preferences: NotRequired[
        "aws_sdk_auto_scaling.types.refresh_preferences.RefreshPreferences"
    ]
    """<p>Sets your preferences for the instance refresh so that it performs as expected when you start it. Includes the instance warmup time, the minimum and maximum healthy percentages, and the behaviors that you want Amazon EC2 Auto Scaling to use if instances that are in <code>Standby</code> state or protected from scale in are found. You can also choose to enable additional features, such as the following:</p> <ul> <li> <p>Auto rollback</p> </li> <li> <p>Checkpoints</p> </li> <li> <p>CloudWatch alarms</p> </li> <li> <p>Skip matching</p> </li> <li> <p>Bake time</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartInstanceRefreshType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "strategy" in value:
        import aws_sdk_auto_scaling.types.refresh_strategy

        aws_sdk_auto_scaling.types.refresh_strategy.serialize_query(
            value["strategy"], pairs, f"{prefix}.Strategy"
        )
    if "desired_configuration" in value:
        import aws_sdk_auto_scaling.types.desired_configuration

        aws_sdk_auto_scaling.types.desired_configuration.serialize_query(
            value["desired_configuration"], pairs, f"{prefix}.DesiredConfiguration"
        )
    if "preferences" in value:
        import aws_sdk_auto_scaling.types.refresh_preferences

        aws_sdk_auto_scaling.types.refresh_preferences.serialize_query(
            value["preferences"], pairs, f"{prefix}.Preferences"
        )


def deserialize_query(el: Element) -> StartInstanceRefreshType:
    out: StartInstanceRefreshType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_strategy = el.find("Strategy")
    if child_strategy is not None:
        import aws_sdk_auto_scaling.types.refresh_strategy

        out["strategy"] = aws_sdk_auto_scaling.types.refresh_strategy.deserialize_query(
            child_strategy
        )
    child_desired_configuration = el.find("DesiredConfiguration")
    if child_desired_configuration is not None:
        import aws_sdk_auto_scaling.types.desired_configuration

        out["desired_configuration"] = (
            aws_sdk_auto_scaling.types.desired_configuration.deserialize_query(
                child_desired_configuration
            )
        )
    child_preferences = el.find("Preferences")
    if child_preferences is not None:
        import aws_sdk_auto_scaling.types.refresh_preferences

        out["preferences"] = (
            aws_sdk_auto_scaling.types.refresh_preferences.deserialize_query(
                child_preferences
            )
        )
    return out
