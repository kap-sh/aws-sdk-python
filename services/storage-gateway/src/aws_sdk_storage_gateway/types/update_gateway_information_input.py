"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateGatewayInformationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cloud_watch_log_group_arn
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.gateway_capacity
    import aws_sdk_storage_gateway.types.gateway_name
    import aws_sdk_storage_gateway.types.gateway_timezone


class UpdateGatewayInformationInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    gateway_name: NotRequired["aws_sdk_storage_gateway.types.gateway_name.GatewayName"]
    gateway_timezone: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_timezone.GatewayTimezone"
    ]
    """<p>A value that indicates the time zone of the gateway.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_storage_gateway.types.cloud_watch_log_group_arn.CloudWatchLogGroupARN"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that you want to use to monitor and log events in the gateway.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html\">What is Amazon CloudWatch Logs?</a> </p>"""
    gateway_capacity: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_capacity.GatewayCapacity"
    ]
    r"""<p>Specifies the size of the gateway's metadata cache. This setting impacts gateway performance and hardware recommendations. For more information, see <a href=\"https://docs.aws.amazon.com/filegateway/latest/files3/performance-multiple-file-shares.html\">Performance guidance for gateways with multiple file shares</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayInformationInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "gateway_name" in value:
        out["GatewayName"] = value["gateway_name"]
    if "gateway_timezone" in value:
        out["GatewayTimezone"] = value["gateway_timezone"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupARN"] = value["cloud_watch_log_group_arn"]
    if "gateway_capacity" in value:
        import aws_sdk_storage_gateway.types.gateway_capacity

        out["GatewayCapacity"] = (
            aws_sdk_storage_gateway.types.gateway_capacity.serialize_aws_json_1_1(
                value["gateway_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayInformationInput:
    out: UpdateGatewayInformationInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("UpdateGatewayInformationInput.gateway_arn required")
    if "GatewayName" in data:
        out["gateway_name"] = data["GatewayName"]
    if "GatewayTimezone" in data:
        out["gateway_timezone"] = data["GatewayTimezone"]
    if "CloudWatchLogGroupARN" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupARN"]
    if "GatewayCapacity" in data:
        import aws_sdk_storage_gateway.types.gateway_capacity

        out["gateway_capacity"] = (
            aws_sdk_storage_gateway.types.gateway_capacity.deserialize_aws_json_1_1(
                data["GatewayCapacity"]
            )
        )
    return out
