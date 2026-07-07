"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListImportFailuresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.import_failure_list
    import aws_sdk_cloudtrail.types.pagination_token


class ListImportFailuresResponse(TypedDict, closed=True):
    failures: NotRequired[
        "aws_sdk_cloudtrail.types.import_failure_list.ImportFailureList"
    ]
    """<p> Contains information about the import failures. </p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImportFailuresResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import aws_sdk_cloudtrail.types.import_failure_list

        out["Failures"] = (
            aws_sdk_cloudtrail.types.import_failure_list.serialize_aws_json_1_1(
                value["failures"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImportFailuresResponse:
    out: ListImportFailuresResponse = {}  # type: ignore[typeddict-item]
    if "Failures" in data:
        import aws_sdk_cloudtrail.types.import_failure_list

        out["failures"] = (
            aws_sdk_cloudtrail.types.import_failure_list.deserialize_aws_json_1_1(
                data["Failures"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
