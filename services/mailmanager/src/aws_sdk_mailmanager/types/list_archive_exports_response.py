"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListArchiveExportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.export_summary_list
    import aws_sdk_mailmanager.types.pagination_token


class ListArchiveExportsResponse(TypedDict):
    exports: NotRequired[
        "aws_sdk_mailmanager.types.export_summary_list.ExportSummaryList"
    ]
    """<p>The list of export job identifiers and statuses.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If present, use to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListArchiveExportsResponse) -> dict:
    out: dict = {}
    if "exports" in value:
        import aws_sdk_mailmanager.types.export_summary_list

        out["Exports"] = (
            aws_sdk_mailmanager.types.export_summary_list.serialize_aws_json_1_0(
                value["exports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListArchiveExportsResponse:
    out: ListArchiveExportsResponse = {}  # type: ignore[typeddict-item]
    if "Exports" in data:
        import aws_sdk_mailmanager.types.export_summary_list

        out["exports"] = (
            aws_sdk_mailmanager.types.export_summary_list.deserialize_aws_json_1_0(
                data["Exports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
