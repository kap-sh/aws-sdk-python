"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListReceivedGrantsForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.grant_list
    import aws_sdk_license_manager.types.string


class ListReceivedGrantsForOrganizationResponse(TypedDict, closed=True):
    grants: NotRequired["aws_sdk_license_manager.types.grant_list.GrantList"]
    """<p>Lists the grants the organization has received.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReceivedGrantsForOrganizationResponse) -> dict:
    out: dict = {}
    if "grants" in value:
        import aws_sdk_license_manager.types.grant_list

        out["Grants"] = aws_sdk_license_manager.types.grant_list.serialize_aws_json_1_1(
            value["grants"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReceivedGrantsForOrganizationResponse:
    out: ListReceivedGrantsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "Grants" in data:
        import aws_sdk_license_manager.types.grant_list

        out["grants"] = (
            aws_sdk_license_manager.types.grant_list.deserialize_aws_json_1_1(
                data["Grants"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
