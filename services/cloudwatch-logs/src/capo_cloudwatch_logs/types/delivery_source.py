"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.delivery_source_configuration
    import capo_cloudwatch_logs.types.delivery_source_name
    import capo_cloudwatch_logs.types.delivery_source_status
    import capo_cloudwatch_logs.types.delivery_source_status_reason
    import capo_cloudwatch_logs.types.log_type
    import capo_cloudwatch_logs.types.resource_arns
    import capo_cloudwatch_logs.types.service
    import capo_cloudwatch_logs.types.tags


class DeliverySource(TypedDict, closed=True):
    name: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    ]
    """<p>The unique name of the delivery source.</p>"""
    arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this delivery source.</p>"""
    resource_arns: NotRequired["capo_cloudwatch_logs.types.resource_arns.ResourceArns"]
    """<p>This array contains the ARN of the Amazon Web Services resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.</p>"""
    service: NotRequired["capo_cloudwatch_logs.types.service.Service"]
    """<p>The Amazon Web Services service that is sending logs.</p>"""
    log_type: NotRequired["capo_cloudwatch_logs.types.log_type.LogType"]
    """<p>The type of log that the source is sending. For valid values for this parameter, see the documentation for the source service.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>The tags that have been assigned to this delivery source.</p>"""
    delivery_source_configuration: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_configuration.DeliverySourceConfiguration"
    ]
    """<p>The map of key-value pairs that configure the delivery source.</p>"""
    status: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_status.DeliverySourceStatus"
    ]
    """<p>The status of the delivery source. A delivery source can have the status <code>ACTIVE</code> or <code>INACTIVE</code>. Note: This value is defined for selective log types.</p>"""
    status_reason: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_status_reason.DeliverySourceStatusReason"
    ]
    """<p>The reason for the status of the delivery source. A status reason of <code>RESOURCE_DELETED</code> indicates that the resource associated with the delivery source has been deleted. Note: This value is defined for selective log types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_arns" in value:
        import capo_cloudwatch_logs.types.resource_arns

        out["resourceArns"] = (
            capo_cloudwatch_logs.types.resource_arns.serialize_aws_json_1_1(
                value["resource_arns"]
            )
        )
    if "service" in value:
        out["service"] = value["service"]
    if "log_type" in value:
        out["logType"] = value["log_type"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "delivery_source_configuration" in value:
        import capo_cloudwatch_logs.types.delivery_source_configuration

        out["deliverySourceConfiguration"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration.serialize_aws_json_1_1(
                value["delivery_source_configuration"]
            )
        )
    if "status" in value:
        import capo_cloudwatch_logs.types.delivery_source_status

        out["status"] = (
            capo_cloudwatch_logs.types.delivery_source_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        import capo_cloudwatch_logs.types.delivery_source_status_reason

        out["statusReason"] = (
            capo_cloudwatch_logs.types.delivery_source_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverySource:
    out: DeliverySource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceArns" in data:
        import capo_cloudwatch_logs.types.resource_arns

        out["resource_arns"] = (
            capo_cloudwatch_logs.types.resource_arns.deserialize_aws_json_1_1(
                data["resourceArns"]
            )
        )
    if "service" in data:
        out["service"] = data["service"]
    if "logType" in data:
        out["log_type"] = data["logType"]
    if "tags" in data:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "deliverySourceConfiguration" in data:
        import capo_cloudwatch_logs.types.delivery_source_configuration

        out["delivery_source_configuration"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration.deserialize_aws_json_1_1(
                data["deliverySourceConfiguration"]
            )
        )
    if "status" in data:
        import capo_cloudwatch_logs.types.delivery_source_status

        out["status"] = (
            capo_cloudwatch_logs.types.delivery_source_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusReason" in data:
        import capo_cloudwatch_logs.types.delivery_source_status_reason

        out["status_reason"] = (
            capo_cloudwatch_logs.types.delivery_source_status_reason.deserialize_aws_json_1_1(
                data["statusReason"]
            )
        )
    return out
