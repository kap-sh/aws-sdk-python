"""Generated from Smithy shape ``com.amazonaws.connect#ListInstanceAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attributes_list
    import capo_connect.types.next_token


class ListInstanceAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired["capo_connect.types.attributes_list.AttributesList"]
    """<p>The attribute types.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstanceAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_connect.types.attributes_list

        out["Attributes"] = capo_connect.types.attributes_list.serialize_json(
            value["attributes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstanceAttributesResponse:
    out: ListInstanceAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_connect.types.attributes_list

        out["attributes"] = capo_connect.types.attributes_list.deserialize_json(
            data["Attributes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
