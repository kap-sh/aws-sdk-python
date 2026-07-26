"""Generated from Smithy shape ``com.amazonaws.odb#ListGiVersionsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListGiVersionsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    shape: NotRequired["str"]
    """<p>The shape to return GI versions for. For a list of valid shapes, use the <code>ListDbSystemShapes</code> operation..</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGiVersionsInput) -> dict:
    out: dict = {}
    if "shape" in value:
        out["shape"] = value["shape"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGiVersionsInput:
    out: ListGiVersionsInput = {}  # type: ignore[typeddict-item]
    if "shape" in data:
        out["shape"] = data["shape"]
    return out
