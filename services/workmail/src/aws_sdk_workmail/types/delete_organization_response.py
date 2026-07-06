"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.string


class DeleteOrganizationResponse(TypedDict, closed=True):
    organization_id: NotRequired[
        "aws_sdk_workmail.types.organization_id.OrganizationId"
    ]
    """<p>The organization ID.</p>"""
    state: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The state of the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationResponse) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationResponse:
    out: DeleteOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "State" in data:
        out["state"] = data["State"]
    return out
