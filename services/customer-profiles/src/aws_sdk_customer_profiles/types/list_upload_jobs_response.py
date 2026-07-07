"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListUploadJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.upload_jobs_list


class ListUploadJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token to use to retrieve the next page of results. </p>"""
    items: NotRequired[
        "aws_sdk_customer_profiles.types.upload_jobs_list.UploadJobsList"
    ]
    """<p>The list of upload jobs for the specified domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUploadJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_customer_profiles.types.upload_jobs_list

        out["Items"] = aws_sdk_customer_profiles.types.upload_jobs_list.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> ListUploadJobsResponse:
    out: ListUploadJobsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.upload_jobs_list

        out["items"] = (
            aws_sdk_customer_profiles.types.upload_jobs_list.deserialize_json(
                data["Items"]
            )
        )
    return out
