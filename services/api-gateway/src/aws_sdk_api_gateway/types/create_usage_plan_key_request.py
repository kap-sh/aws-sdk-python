"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateUsagePlanKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class CreateUsagePlanKeyRequest(TypedDict):
    usage_plan_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.</p>"""
    key_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of a UsagePlanKey resource for a plan customer.</p>"""
    key_type: "aws_sdk_api_gateway.types.string.String"
    """<p>The type of a UsagePlanKey resource for a plan customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUsagePlanKeyRequest) -> dict:
    out: dict = {}
    out["keyId"] = value["key_id"]
    out["keyType"] = value["key_type"]
    return out


def deserialize_json(data: dict) -> CreateUsagePlanKeyRequest:
    out: CreateUsagePlanKeyRequest = {}  # type: ignore[typeddict-item]
    if "keyId" in data:
        out["key_id"] = data["keyId"]
    else:
        raise DeserializationError("CreateUsagePlanKeyRequest.key_id required")
    if "keyType" in data:
        out["key_type"] = data["keyType"]
    else:
        raise DeserializationError("CreateUsagePlanKeyRequest.key_type required")
    return out
