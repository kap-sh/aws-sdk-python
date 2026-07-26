"""Generated from Smithy shape ``com.amazonaws.workmail#GetDefaultRetentionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.organization_id


class GetDefaultRetentionPolicyRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDefaultRetentionPolicyRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDefaultRetentionPolicyRequest:
    out: GetDefaultRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "GetDefaultRetentionPolicyRequest.organization_id required"
        )
    return out
