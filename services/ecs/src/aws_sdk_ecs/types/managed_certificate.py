"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedCertificate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedCertificate(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the ACM certificate.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the ACM; certificate.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the ACM certificate is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the ACM certificate was last updated</p>"""
    domain_name: "aws_sdk_ecs.types.string.String"
    """<p>The fully qualified domain name (FQDN) that is secured with this ACM certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedCertificate) -> dict:
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
    out["domainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedCertificate:
    out: ManagedCertificate = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("ManagedCertificate.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedCertificate.updated_at required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("ManagedCertificate.domain_name required")
    return out
