"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListAddressListImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.import_jobs
    import aws_sdk_mailmanager.types.pagination_token


class ListAddressListImportJobsResponse(TypedDict, closed=True):
    import_jobs: "aws_sdk_mailmanager.types.import_jobs.ImportJobs"
    """<p>The list of import jobs.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAddressListImportJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.import_jobs

    out["ImportJobs"] = aws_sdk_mailmanager.types.import_jobs.serialize_aws_json_1_0(
        value["import_jobs"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAddressListImportJobsResponse:
    out: ListAddressListImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobs" in data:
        import aws_sdk_mailmanager.types.import_jobs

        out["import_jobs"] = (
            aws_sdk_mailmanager.types.import_jobs.deserialize_aws_json_1_0(
                data["ImportJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListAddressListImportJobsResponse.import_jobs required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
