"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteRetentionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.short_string


class DeleteRetentionPolicyRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""
    id: "aws_sdk_workmail.types.short_string.ShortString"
    """<p>The retention policy ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRetentionPolicyRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRetentionPolicyRequest:
    out: DeleteRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteRetentionPolicyRequest.organization_id required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteRetentionPolicyRequest.id required")
    return out
