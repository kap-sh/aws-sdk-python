"""Generated from Smithy shape ``com.amazonaws.shield#AssociateHealthCheckRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.health_check_arn
    import aws_sdk_shield.types.protection_id


class AssociateHealthCheckRequest(TypedDict):
    protection_id: "aws_sdk_shield.types.protection_id.ProtectionId"
    """<p>The unique identifier (ID) for the <a>Protection</a> object to add the health check association to. </p>"""
    health_check_arn: "aws_sdk_shield.types.health_check_arn.HealthCheckArn"
    """<p>The Amazon Resource Name (ARN) of the health check to associate with the protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateHealthCheckRequest) -> dict:
    out: dict = {}
    out["ProtectionId"] = value["protection_id"]
    out["HealthCheckArn"] = value["health_check_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateHealthCheckRequest:
    out: AssociateHealthCheckRequest = {}  # type: ignore[typeddict-item]
    if "ProtectionId" in data:
        out["protection_id"] = data["ProtectionId"]
    else:
        raise DeserializationError("AssociateHealthCheckRequest.protection_id required")
    if "HealthCheckArn" in data:
        out["health_check_arn"] = data["HealthCheckArn"]
    else:
        raise DeserializationError(
            "AssociateHealthCheckRequest.health_check_arn required"
        )
    return out
