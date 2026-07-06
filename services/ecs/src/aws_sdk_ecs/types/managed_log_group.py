"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedLogGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedLogGroup(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Cloudwatch Log Group associated with the Express service.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the Cloudwatch LogGroup.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the Cloudwatch LogGroup is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the Cloudwatch LogGroup was last updated</p>"""
    log_group_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the Cloudwatch Log Group associated with the Express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLogGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import aws_sdk_ecs.types.managed_resource_status

    out["status"] = aws_sdk_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_ecs.types.timestamp

    out["updatedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedLogGroup:
    out: ManagedLogGroup = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import aws_sdk_ecs.types.managed_resource_status

        out["status"] = (
            aws_sdk_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ManagedLogGroup.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedLogGroup.updated_at required")
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("ManagedLogGroup.log_group_name required")
    return out
