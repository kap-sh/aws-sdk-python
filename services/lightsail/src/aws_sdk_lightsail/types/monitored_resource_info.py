"""Generated from Smithy shape ``com.amazonaws.lightsail#MonitoredResourceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_arn
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type


class MonitoredResourceInfo(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_lightsail.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource being monitored.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the Lightsail resource being monitored.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type of the resource being monitored.</p> <p>Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoredResourceInfo) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoredResourceInfo:
    out: MonitoredResourceInfo = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    return out
