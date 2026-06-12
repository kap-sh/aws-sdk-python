"""Generated from Smithy shape ``com.amazonaws.workmail#PutInboundDmarcSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean_object
    import aws_sdk_workmail.types.organization_id


class PutInboundDmarcSettingsRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The ID of the organization that you are applying the DMARC policy to.</p>"""
    enforced: "aws_sdk_workmail.types.boolean_object.BooleanObject"
    """<p>Enforces or suspends a policy after it's applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInboundDmarcSettingsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Enforced"] = value["enforced"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInboundDmarcSettingsRequest:
    out: PutInboundDmarcSettingsRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "PutInboundDmarcSettingsRequest.organization_id required"
        )
    if "Enforced" in data:
        out["enforced"] = data["Enforced"]
    else:
        raise DeserializationError("PutInboundDmarcSettingsRequest.enforced required")
    return out
