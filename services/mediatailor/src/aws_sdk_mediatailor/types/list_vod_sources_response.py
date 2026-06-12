"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListVodSourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_vod_source
    import aws_sdk_mediatailor.types.__string


class ListVodSourcesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_vod_source.__listOfVodSource"
    ]
    """<p>Lists the VOD sources.</p>"""
    next_token: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVodSourcesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediatailor.types.__list_of_vod_source

        out["Items"] = aws_sdk_mediatailor.types.__list_of_vod_source.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVodSourcesResponse:
    out: ListVodSourcesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediatailor.types.__list_of_vod_source

        out["items"] = aws_sdk_mediatailor.types.__list_of_vod_source.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
