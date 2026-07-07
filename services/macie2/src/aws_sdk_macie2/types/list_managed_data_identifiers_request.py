"""Generated from Smithy shape ``com.amazonaws.macie2#ListManagedDataIdentifiersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class ListManagedDataIdentifiersRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedDataIdentifiersRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedDataIdentifiersRequest:
    out: ListManagedDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
