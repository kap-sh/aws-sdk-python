"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.row_list


class ListMetricsResponse(TypedDict, closed=True):
    rows: "capo_resiliencehub.types.row_list.RowList"
    """<p>Specifies all the list of metric values for each row of metrics.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetricsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.row_list

    out["rows"] = capo_resiliencehub.types.row_list.serialize_json(value["rows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMetricsResponse:
    out: ListMetricsResponse = {}  # type: ignore[typeddict-item]
    if "rows" in data:
        import capo_resiliencehub.types.row_list

        out["rows"] = capo_resiliencehub.types.row_list.deserialize_json(data["rows"])
    else:
        raise DeserializationError("ListMetricsResponse.rows required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
