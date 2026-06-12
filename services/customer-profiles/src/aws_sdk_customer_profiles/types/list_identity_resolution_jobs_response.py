"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListIdentityResolutionJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.identity_resolution_jobs_list
    import aws_sdk_customer_profiles.types.token


class ListIdentityResolutionJobsResponse(TypedDict):
    identity_resolution_jobs_list: NotRequired[
        "aws_sdk_customer_profiles.types.identity_resolution_jobs_list.IdentityResolutionJobsList"
    ]
    """<p>A list of Identity Resolution Jobs.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityResolutionJobsResponse) -> dict:
    out: dict = {}
    if "identity_resolution_jobs_list" in value:
        import aws_sdk_customer_profiles.types.identity_resolution_jobs_list

        out["IdentityResolutionJobsList"] = (
            aws_sdk_customer_profiles.types.identity_resolution_jobs_list.serialize_json(
                value["identity_resolution_jobs_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdentityResolutionJobsResponse:
    out: ListIdentityResolutionJobsResponse = {}  # type: ignore[typeddict-item]
    if "IdentityResolutionJobsList" in data:
        import aws_sdk_customer_profiles.types.identity_resolution_jobs_list

        out["identity_resolution_jobs_list"] = (
            aws_sdk_customer_profiles.types.identity_resolution_jobs_list.deserialize_json(
                data["IdentityResolutionJobsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
