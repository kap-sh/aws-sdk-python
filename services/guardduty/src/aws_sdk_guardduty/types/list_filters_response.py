"""Generated from Smithy shape ``com.amazonaws.guardduty#ListFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.filter_names
    import aws_sdk_guardduty.types.string


class ListFiltersResponse(TypedDict, closed=True):
    filter_names: NotRequired["aws_sdk_guardduty.types.filter_names.FilterNames"]
    """<p>A list of filter names.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFiltersResponse) -> dict:
    out: dict = {}
    if "filter_names" in value:
        import aws_sdk_guardduty.types.filter_names

        out["filterNames"] = aws_sdk_guardduty.types.filter_names.serialize_json(
            value["filter_names"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFiltersResponse:
    out: ListFiltersResponse = {}  # type: ignore[typeddict-item]
    if "filterNames" in data:
        import aws_sdk_guardduty.types.filter_names

        out["filter_names"] = aws_sdk_guardduty.types.filter_names.deserialize_json(
            data["filterNames"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
