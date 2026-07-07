"""Generated from Smithy shape ``com.amazonaws.workmail#CreateOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id


class CreateOrganizationResponse(TypedDict, closed=True):
    organization_id: NotRequired[
        "aws_sdk_workmail.types.organization_id.OrganizationId"
    ]
    """<p>The organization ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOrganizationResponse) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOrganizationResponse:
    out: CreateOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    return out
