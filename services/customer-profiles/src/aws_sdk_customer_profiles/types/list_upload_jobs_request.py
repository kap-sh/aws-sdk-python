"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListUploadJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size500
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token


class ListUploadJobsRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain to list upload jobs for. </p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size500.MaxSize500"]
    """<p>The maximum number of upload jobs to return per page. </p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUploadJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUploadJobsRequest:
    out: ListUploadJobsRequest = {}  # type: ignore[typeddict-item]
    return out
