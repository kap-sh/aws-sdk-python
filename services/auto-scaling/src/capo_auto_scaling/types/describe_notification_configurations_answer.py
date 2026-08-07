"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeNotificationConfigurationsAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.notification_configurations
    import capo_auto_scaling.types.xml_string


class DescribeNotificationConfigurationsAnswer(TypedDict, closed=True):
    notification_configurations: NotRequired[
        "capo_auto_scaling.types.notification_configurations.NotificationConfigurations"
    ]
    """<p>The notification configurations.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeNotificationConfigurationsAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "notification_configurations" in value:
        import capo_auto_scaling.types.notification_configurations

        capo_auto_scaling.types.notification_configurations.serialize_query(
            value["notification_configurations"],
            pairs,
            f"{key_prefix}NotificationConfigurations",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeNotificationConfigurationsAnswer:
    out: DescribeNotificationConfigurationsAnswer = {}  # type: ignore[typeddict-item]
    child_notification_configurations = el.find("NotificationConfigurations")
    if child_notification_configurations is not None:
        import capo_auto_scaling.types.notification_configurations

        out["notification_configurations"] = (
            capo_auto_scaling.types.notification_configurations.deserialize_query(
                child_notification_configurations
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
