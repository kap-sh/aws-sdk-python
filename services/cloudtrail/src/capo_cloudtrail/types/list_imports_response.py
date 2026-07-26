"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListImportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.imports_list
    import capo_cloudtrail.types.pagination_token


class ListImportsResponse(TypedDict, closed=True):
    imports: NotRequired["capo_cloudtrail.types.imports_list.ImportsList"]
    """<p> The list of returned imports. </p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of import results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImportsResponse) -> dict:
    out: dict = {}
    if "imports" in value:
        import capo_cloudtrail.types.imports_list

        out["Imports"] = capo_cloudtrail.types.imports_list.serialize_aws_json_1_1(
            value["imports"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImportsResponse:
    out: ListImportsResponse = {}  # type: ignore[typeddict-item]
    if "Imports" in data:
        import capo_cloudtrail.types.imports_list

        out["imports"] = capo_cloudtrail.types.imports_list.deserialize_aws_json_1_1(
            data["Imports"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
