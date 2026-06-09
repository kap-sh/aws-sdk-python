"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointConnectionNotificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list
    import aws_sdk_ec2.types.vpc_endpoint_id
    import aws_sdk_ec2.types.vpc_endpoint_service_id


class CreateVpcEndpointConnectionNotificationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the endpoint service.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the endpoint.</p>"""
    connection_notification_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the SNS topic for the notifications.</p>"""
    connection_events: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The endpoint events for which to receive notifications. Valid values are <code>Accept</code>, <code>Connect</code>, <code>Delete</code>, and <code>Reject</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEndpointConnectionNotificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "service_id" in value:
        pairs.append((f"{prefix}.ServiceId", str(value["service_id"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{prefix}.VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "connection_notification_arn" in value:
        pairs.append(
            (
                f"{prefix}.ConnectionNotificationArn",
                str(value["connection_notification_arn"]),
            )
        )
    if "connection_events" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["connection_events"], pairs, f"{prefix}.ConnectionEvents"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(
    el: Element,
) -> CreateVpcEndpointConnectionNotificationRequest:
    out: CreateVpcEndpointConnectionNotificationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_connection_notification_arn = el.find("ConnectionNotificationArn")
    if child_connection_notification_arn is not None:
        out["connection_notification_arn"] = str(
            child_connection_notification_arn.text or ""
        )
    if el.find("ConnectionEvents") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["connection_events"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ConnectionEvents"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
