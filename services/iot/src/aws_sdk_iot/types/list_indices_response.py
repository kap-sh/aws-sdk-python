"""Generated from Smithy shape ``com.amazonaws.iot#ListIndicesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.index_names_list
    import aws_sdk_iot.types.next_token


class ListIndicesResponse(TypedDict):
    index_names: NotRequired["aws_sdk_iot.types.index_names_list.IndexNamesList"]
    """<p>The index names.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token used to get the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndicesResponse) -> dict:
    out: dict = {}
    if "index_names" in value:
        import aws_sdk_iot.types.index_names_list

        out["indexNames"] = aws_sdk_iot.types.index_names_list.serialize_json(
            value["index_names"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIndicesResponse:
    out: ListIndicesResponse = {}  # type: ignore[typeddict-item]
    if "indexNames" in data:
        import aws_sdk_iot.types.index_names_list

        out["index_names"] = aws_sdk_iot.types.index_names_list.deserialize_json(
            data["indexNames"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
