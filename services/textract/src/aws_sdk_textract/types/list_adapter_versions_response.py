"""Generated from Smithy shape ``com.amazonaws.textract#ListAdapterVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_version_list
    import aws_sdk_textract.types.pagination_token


class ListAdapterVersionsResponse(TypedDict, closed=True):
    adapter_versions: NotRequired[
        "aws_sdk_textract.types.adapter_version_list.AdapterVersionList"
    ]
    """<p>Adapter versions that match the filtering criteria specified when calling ListAdapters.</p>"""
    next_token: NotRequired["aws_sdk_textract.types.pagination_token.PaginationToken"]
    """<p>Identifies the next page of results to return when listing adapter versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAdapterVersionsResponse) -> dict:
    out: dict = {}
    if "adapter_versions" in value:
        import aws_sdk_textract.types.adapter_version_list

        out["AdapterVersions"] = (
            aws_sdk_textract.types.adapter_version_list.serialize_aws_json_1_1(
                value["adapter_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAdapterVersionsResponse:
    out: ListAdapterVersionsResponse = {}  # type: ignore[typeddict-item]
    if "AdapterVersions" in data:
        import aws_sdk_textract.types.adapter_version_list

        out["adapter_versions"] = (
            aws_sdk_textract.types.adapter_version_list.deserialize_aws_json_1_1(
                data["AdapterVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
