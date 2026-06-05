"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionNotificationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_notification_id
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointConnectionNotificationsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    connection_notification_id: NotRequired[
        "aws_sdk_ec2.types.connection_notification_id.ConnectionNotificationId"
    ]
    """<p>The ID of the notification.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>connection-notification-arn</code> - The ARN of the SNS topic for the notification.</p> </li> <li> <p> <code>connection-notification-id</code> - The ID of the notification.</p> </li> <li> <p> <code>connection-notification-state</code> - The state of the notification (<code>Enabled</code> | <code>Disabled</code>).</p> </li> <li> <p> <code>connection-notification-type</code> - The type of notification (<code>Topic</code>).</p> </li> <li> <p> <code>service-id</code> - The ID of the endpoint service.</p> </li> <li> <p> <code>vpc-endpoint-id</code> - The ID of the VPC endpoint.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another request with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointConnectionNotificationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "connection_notification_id" in value:
        pairs.append(
            (
                f"{prefix}.ConnectionNotificationId",
                str(value["connection_notification_id"]),
            )
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeVpcEndpointConnectionNotificationsRequest:
    out: DescribeVpcEndpointConnectionNotificationsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_connection_notification_id = el.find("ConnectionNotificationId")
    if child_connection_notification_id is not None:
        out["connection_notification_id"] = str(
            child_connection_notification_id.text or ""
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
