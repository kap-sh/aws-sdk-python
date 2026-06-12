"""Generated from Smithy shape ``com.amazonaws.workmail#ListAccessControlRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id


class ListAccessControlRulesRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessControlRulesRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessControlRulesRequest:
    out: ListAccessControlRulesRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "ListAccessControlRulesRequest.organization_id required"
        )
    return out
