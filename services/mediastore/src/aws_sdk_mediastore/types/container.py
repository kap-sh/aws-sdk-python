"""Generated from Smithy shape ``com.amazonaws.mediastore#Container``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_access_logging_enabled
    import aws_sdk_mediastore.types.container_arn
    import aws_sdk_mediastore.types.container_name
    import aws_sdk_mediastore.types.container_status
    import aws_sdk_mediastore.types.endpoint
    import aws_sdk_mediastore.types.time_stamp


class Container(TypedDict, closed=True):
    endpoint: NotRequired["aws_sdk_mediastore.types.endpoint.Endpoint"]
    """<p>The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.</p>"""
    creation_time: NotRequired["aws_sdk_mediastore.types.time_stamp.TimeStamp"]
    """<p>Unix timestamp.</p>"""
    arn: NotRequired["aws_sdk_mediastore.types.container_arn.ContainerARN"]
    """<p>The Amazon Resource Name (ARN) of the container. The ARN has the following format:</p> <p>arn:aws:<region>:<account that owns this container>:container/<name of container> </p> <p>For example: arn:aws:mediastore:us-west-2:111122223333:container/movies </p>"""
    name: NotRequired["aws_sdk_mediastore.types.container_name.ContainerName"]
    """<p>The name of the container.</p>"""
    status: NotRequired["aws_sdk_mediastore.types.container_status.ContainerStatus"]
    """<p>The status of container creation or deletion. The status is one of the following: <code>CREATING</code>, <code>ACTIVE</code>, or <code>DELETING</code>. While the service is creating the container, the status is <code>CREATING</code>. When the endpoint is available, the status changes to <code>ACTIVE</code>.</p>"""
    access_logging_enabled: NotRequired[
        "aws_sdk_mediastore.types.container_access_logging_enabled.ContainerAccessLoggingEnabled"
    ]
    """<p>The state of access logging on the container. This value is <code>false</code> by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to <code>true</code>, indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Container) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "creation_time" in value:
        import aws_sdk_mediastore.types.time_stamp

        out["CreationTime"] = (
            aws_sdk_mediastore.types.time_stamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_mediastore.types.container_status

        out["Status"] = (
            aws_sdk_mediastore.types.container_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "access_logging_enabled" in value:
        out["AccessLoggingEnabled"] = value["access_logging_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Container:
    out: Container = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "CreationTime" in data:
        import aws_sdk_mediastore.types.time_stamp

        out["creation_time"] = (
            aws_sdk_mediastore.types.time_stamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_mediastore.types.container_status

        out["status"] = (
            aws_sdk_mediastore.types.container_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "AccessLoggingEnabled" in data:
        out["access_logging_enabled"] = data["AccessLoggingEnabled"]
    return out
