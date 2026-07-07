"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionNotificationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification_set
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointConnectionNotificationsResult(TypedDict, closed=True):
    connection_notification_set: NotRequired[
        "aws_sdk_ec2.types.connection_notification_set.ConnectionNotificationSet"
    ]
    """<p>The notifications.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointConnectionNotificationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "connection_notification_set" in value:
        import aws_sdk_ec2.types.connection_notification_set

        aws_sdk_ec2.types.connection_notification_set.serialize_ec2_query(
            value["connection_notification_set"],
            pairs,
            f"{prefix}.ConnectionNotificationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeVpcEndpointConnectionNotificationsResult:
    out: DescribeVpcEndpointConnectionNotificationsResult = {}  # type: ignore[typeddict-item]
    if el.find("ConnectionNotificationSet") is not None:
        import aws_sdk_ec2.types.connection_notification_set

        out["connection_notification_set"] = (
            aws_sdk_ec2.types.connection_notification_set.deserialize_ec2_query(
                el, "ConnectionNotificationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
