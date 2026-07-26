"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.managed_resource_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ManagedSecurityGroup(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the security group.</p>"""
    status: "capo_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the security group.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the security group is in the current status.</p>"""
    updated_at: "capo_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the security group was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedSecurityGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import capo_ecs.types.managed_resource_status

    out["status"] = capo_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_ecs.types.timestamp

    out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedSecurityGroup:
    out: ManagedSecurityGroup = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import capo_ecs.types.managed_resource_status

        out["status"] = capo_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        raise DeserializationError("ManagedSecurityGroup.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedSecurityGroup.updated_at required")
    return out
