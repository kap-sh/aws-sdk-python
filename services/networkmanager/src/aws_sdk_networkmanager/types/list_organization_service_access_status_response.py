"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListOrganizationServiceAccessStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.organization_status


class ListOrganizationServiceAccessStatusResponse(TypedDict):
    organization_status: NotRequired[
        "aws_sdk_networkmanager.types.organization_status.OrganizationStatus"
    ]
    """<p>Displays the status of an Amazon Web Services Organization.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationServiceAccessStatusResponse) -> dict:
    out: dict = {}
    if "organization_status" in value:
        import aws_sdk_networkmanager.types.organization_status

        out["OrganizationStatus"] = (
            aws_sdk_networkmanager.types.organization_status.serialize_json(
                value["organization_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationServiceAccessStatusResponse:
    out: ListOrganizationServiceAccessStatusResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationStatus" in data:
        import aws_sdk_networkmanager.types.organization_status

        out["organization_status"] = (
            aws_sdk_networkmanager.types.organization_status.deserialize_json(
                data["OrganizationStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
