"""Generated from Smithy shape ``com.amazonaws.inspector2#ListUsageTotalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.list_usage_totals_next_token
    import aws_sdk_inspector2.types.usage_total_list


class ListUsageTotalsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_inspector2.types.list_usage_totals_next_token.ListUsageTotalsNextToken"
    ]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""
    totals: NotRequired["aws_sdk_inspector2.types.usage_total_list.UsageTotalList"]
    """<p>An object with details on the total usage for the requested account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsageTotalsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "totals" in value:
        import aws_sdk_inspector2.types.usage_total_list

        out["totals"] = aws_sdk_inspector2.types.usage_total_list.serialize_json(
            value["totals"]
        )
    return out


def deserialize_json(data: dict) -> ListUsageTotalsResponse:
    out: ListUsageTotalsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "totals" in data:
        import aws_sdk_inspector2.types.usage_total_list

        out["totals"] = aws_sdk_inspector2.types.usage_total_list.deserialize_json(
            data["totals"]
        )
    return out
