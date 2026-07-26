"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListDistributedGrantsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.grant_list
    import capo_license_manager.types.string


class ListDistributedGrantsResponse(TypedDict, closed=True):
    grants: NotRequired["capo_license_manager.types.grant_list.GrantList"]
    """<p>Distributed grant details.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDistributedGrantsResponse) -> dict:
    out: dict = {}
    if "grants" in value:
        import capo_license_manager.types.grant_list

        out["Grants"] = capo_license_manager.types.grant_list.serialize_aws_json_1_1(
            value["grants"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDistributedGrantsResponse:
    out: ListDistributedGrantsResponse = {}  # type: ignore[typeddict-item]
    if "Grants" in data:
        import capo_license_manager.types.grant_list

        out["grants"] = capo_license_manager.types.grant_list.deserialize_aws_json_1_1(
            data["Grants"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
