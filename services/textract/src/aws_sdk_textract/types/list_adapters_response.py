"""Generated from Smithy shape ``com.amazonaws.textract#ListAdaptersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_list
    import aws_sdk_textract.types.pagination_token


class ListAdaptersResponse(TypedDict):
    adapters: NotRequired["aws_sdk_textract.types.adapter_list.AdapterList"]
    """<p>A list of adapters that matches the filtering criteria specified when calling ListAdapters.</p>"""
    next_token: NotRequired["aws_sdk_textract.types.pagination_token.PaginationToken"]
    """<p>Identifies the next page of results to return when listing adapters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAdaptersResponse) -> dict:
    out: dict = {}
    if "adapters" in value:
        import aws_sdk_textract.types.adapter_list

        out["Adapters"] = aws_sdk_textract.types.adapter_list.serialize_aws_json_1_1(
            value["adapters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAdaptersResponse:
    out: ListAdaptersResponse = {}  # type: ignore[typeddict-item]
    if "Adapters" in data:
        import aws_sdk_textract.types.adapter_list

        out["adapters"] = aws_sdk_textract.types.adapter_list.deserialize_aws_json_1_1(
            data["Adapters"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
