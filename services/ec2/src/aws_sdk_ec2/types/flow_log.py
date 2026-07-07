"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.destination_options_response
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.log_destination_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.traffic_type


class FlowLog(TypedDict, closed=True):
    creation_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the flow log was created.</p>"""
    deliver_logs_error_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Information about the error that occurred. <code>Rate limited</code> indicates that CloudWatch Logs throttling has been applied for one or more network interfaces, or that you've reached the limit on the number of log groups that you can create. <code>Access error</code> indicates that the IAM role associated with the flow log does not have sufficient permissions to publish to CloudWatch Logs. <code>Unknown error</code> indicates an internal error.</p>"""
    deliver_logs_permission_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the IAM role allows the service to publish logs to CloudWatch Logs.</p>"""
    deliver_cross_account_role: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the IAM role that allows the service to publish flow logs across accounts.</p>"""
    deliver_logs_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the logs delivery (<code>SUCCESS</code> | <code>FAILED</code>).</p>"""
    flow_log_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the flow log.</p>"""
    flow_log_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the flow log (<code>ACTIVE</code>).</p>"""
    log_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the flow log group.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource being monitored.</p>"""
    traffic_type: NotRequired["aws_sdk_ec2.types.traffic_type.TrafficType"]
    """<p>The type of traffic captured for the flow log.</p>"""
    log_destination_type: NotRequired[
        "aws_sdk_ec2.types.log_destination_type.LogDestinationType"
    ]
    """<p>The type of destination for the flow log data.</p>"""
    log_destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the destination for the flow log data.</p>"""
    log_format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the flow log record.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the flow log.</p>"""
    max_aggregation_interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    r"""<p>The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.</p> <p>When a network interface is attached to a <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\">Nitro-based instance</a>, the aggregation interval is always 60 seconds (1 minute) or less, regardless of the specified value.</p> <p>Valid Values: <code>60</code> | <code>600</code> </p>"""
    destination_options: NotRequired[
        "aws_sdk_ec2.types.destination_options_response.DestinationOptionsResponse"
    ]
    """<p>The destination options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlowLog, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "creation_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "deliver_logs_error_message" in value:
        pairs.append(
            (
                f"{prefix}.DeliverLogsErrorMessage",
                str(value["deliver_logs_error_message"]),
            )
        )
    if "deliver_logs_permission_arn" in value:
        pairs.append(
            (
                f"{prefix}.DeliverLogsPermissionArn",
                str(value["deliver_logs_permission_arn"]),
            )
        )
    if "deliver_cross_account_role" in value:
        pairs.append(
            (
                f"{prefix}.DeliverCrossAccountRole",
                str(value["deliver_cross_account_role"]),
            )
        )
    if "deliver_logs_status" in value:
        pairs.append((f"{prefix}.DeliverLogsStatus", str(value["deliver_logs_status"])))
    if "flow_log_id" in value:
        pairs.append((f"{prefix}.FlowLogId", str(value["flow_log_id"])))
    if "flow_log_status" in value:
        pairs.append((f"{prefix}.FlowLogStatus", str(value["flow_log_status"])))
    if "log_group_name" in value:
        pairs.append((f"{prefix}.LogGroupName", str(value["log_group_name"])))
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "traffic_type" in value:
        import aws_sdk_ec2.types.traffic_type

        aws_sdk_ec2.types.traffic_type.serialize_ec2_query(
            value["traffic_type"], pairs, f"{prefix}.TrafficType"
        )
    if "log_destination_type" in value:
        import aws_sdk_ec2.types.log_destination_type

        aws_sdk_ec2.types.log_destination_type.serialize_ec2_query(
            value["log_destination_type"], pairs, f"{prefix}.LogDestinationType"
        )
    if "log_destination" in value:
        pairs.append((f"{prefix}.LogDestination", str(value["log_destination"])))
    if "log_format" in value:
        pairs.append((f"{prefix}.LogFormat", str(value["log_format"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "max_aggregation_interval" in value:
        pairs.append(
            (f"{prefix}.MaxAggregationInterval", str(value["max_aggregation_interval"]))
        )
    if "destination_options" in value:
        import aws_sdk_ec2.types.destination_options_response

        aws_sdk_ec2.types.destination_options_response.serialize_ec2_query(
            value["destination_options"], pairs, f"{prefix}.DestinationOptions"
        )


def deserialize_ec2_query(el: Element) -> FlowLog:
    out: FlowLog = {}  # type: ignore[typeddict-item]
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["creation_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_time
            )
        )
    child_deliver_logs_error_message = el.find("DeliverLogsErrorMessage")
    if child_deliver_logs_error_message is not None:
        out["deliver_logs_error_message"] = str(
            child_deliver_logs_error_message.text or ""
        )
    child_deliver_logs_permission_arn = el.find("DeliverLogsPermissionArn")
    if child_deliver_logs_permission_arn is not None:
        out["deliver_logs_permission_arn"] = str(
            child_deliver_logs_permission_arn.text or ""
        )
    child_deliver_cross_account_role = el.find("DeliverCrossAccountRole")
    if child_deliver_cross_account_role is not None:
        out["deliver_cross_account_role"] = str(
            child_deliver_cross_account_role.text or ""
        )
    child_deliver_logs_status = el.find("DeliverLogsStatus")
    if child_deliver_logs_status is not None:
        out["deliver_logs_status"] = str(child_deliver_logs_status.text or "")
    child_flow_log_id = el.find("FlowLogId")
    if child_flow_log_id is not None:
        out["flow_log_id"] = str(child_flow_log_id.text or "")
    child_flow_log_status = el.find("FlowLogStatus")
    if child_flow_log_status is not None:
        out["flow_log_status"] = str(child_flow_log_status.text or "")
    child_log_group_name = el.find("LogGroupName")
    if child_log_group_name is not None:
        out["log_group_name"] = str(child_log_group_name.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_traffic_type = el.find("TrafficType")
    if child_traffic_type is not None:
        import aws_sdk_ec2.types.traffic_type

        out["traffic_type"] = aws_sdk_ec2.types.traffic_type.deserialize_ec2_query(
            child_traffic_type
        )
    child_log_destination_type = el.find("LogDestinationType")
    if child_log_destination_type is not None:
        import aws_sdk_ec2.types.log_destination_type

        out["log_destination_type"] = (
            aws_sdk_ec2.types.log_destination_type.deserialize_ec2_query(
                child_log_destination_type
            )
        )
    child_log_destination = el.find("LogDestination")
    if child_log_destination is not None:
        out["log_destination"] = str(child_log_destination.text or "")
    child_log_format = el.find("LogFormat")
    if child_log_format is not None:
        out["log_format"] = str(child_log_format.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_max_aggregation_interval = el.find("MaxAggregationInterval")
    if child_max_aggregation_interval is not None:
        out["max_aggregation_interval"] = int(child_max_aggregation_interval.text or "")
    child_destination_options = el.find("DestinationOptions")
    if child_destination_options is not None:
        import aws_sdk_ec2.types.destination_options_response

        out["destination_options"] = (
            aws_sdk_ec2.types.destination_options_response.deserialize_ec2_query(
                child_destination_options
            )
        )
    return out
