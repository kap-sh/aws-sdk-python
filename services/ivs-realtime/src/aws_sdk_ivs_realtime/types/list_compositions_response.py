"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListCompositionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition_summary_list
    import aws_sdk_ivs_realtime.types.pagination_token


class ListCompositionsResponse(TypedDict):
    compositions: (
        "aws_sdk_ivs_realtime.types.composition_summary_list.CompositionSummaryList"
    )
    """<p>List of the matching Compositions (summary information only).</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more compositions than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCompositionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.composition_summary_list

    out["compositions"] = (
        aws_sdk_ivs_realtime.types.composition_summary_list.serialize_json(
            value["compositions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCompositionsResponse:
    out: ListCompositionsResponse = {}  # type: ignore[typeddict-item]
    if "compositions" in data:
        import aws_sdk_ivs_realtime.types.composition_summary_list

        out["compositions"] = (
            aws_sdk_ivs_realtime.types.composition_summary_list.deserialize_json(
                data["compositions"]
            )
        )
    else:
        raise DeserializationError("ListCompositionsResponse.compositions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
