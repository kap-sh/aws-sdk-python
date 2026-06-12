"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateHealthCheckRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.health_check_arn
    import aws_sdk_shield.types.protection_id


class DisassociateHealthCheckRequest(TypedDict):
    protection_id: "aws_sdk_shield.types.protection_id.ProtectionId"
    """<p>The unique identifier (ID) for the <a>Protection</a> object to remove the health check association from. </p>"""
    health_check_arn: "aws_sdk_shield.types.health_check_arn.HealthCheckArn"
    """<p>The Amazon Resource Name (ARN) of the health check that is associated with the protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateHealthCheckRequest) -> dict:
    out: dict = {}
    out["ProtectionId"] = value["protection_id"]
    out["HealthCheckArn"] = value["health_check_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateHealthCheckRequest:
    out: DisassociateHealthCheckRequest = {}  # type: ignore[typeddict-item]
    if "ProtectionId" in data:
        out["protection_id"] = data["ProtectionId"]
    else:
        raise DeserializationError(
            "DisassociateHealthCheckRequest.protection_id required"
        )
    if "HealthCheckArn" in data:
        out["health_check_arn"] = data["HealthCheckArn"]
    else:
        raise DeserializationError(
            "DisassociateHealthCheckRequest.health_check_arn required"
        )
    return out
