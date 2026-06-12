"""Generated from Smithy shape ``com.amazonaws.organizations#CreateOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.organization


class CreateOrganizationResponse(TypedDict):
    organization: NotRequired["aws_sdk_organizations.types.organization.Organization"]
    """<p>A structure that contains details about the newly created organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOrganizationResponse) -> dict:
    out: dict = {}
    if "organization" in value:
        import aws_sdk_organizations.types.organization

        out["Organization"] = (
            aws_sdk_organizations.types.organization.serialize_aws_json_1_1(
                value["organization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOrganizationResponse:
    out: CreateOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "Organization" in data:
        import aws_sdk_organizations.types.organization

        out["organization"] = (
            aws_sdk_organizations.types.organization.deserialize_aws_json_1_1(
                data["Organization"]
            )
        )
    return out
