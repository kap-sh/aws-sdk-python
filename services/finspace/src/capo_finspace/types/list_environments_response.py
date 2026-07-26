"""Generated from Smithy shape ``com.amazonaws.finspace#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.environment_list
    import capo_finspace.types.pagination_token


class ListEnvironmentsResponse(TypedDict, closed=True):
    environments: NotRequired["capo_finspace.types.environment_list.EnvironmentList"]
    """<p>A list of all of your FinSpace environments.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    if "environments" in value:
        import capo_finspace.types.environment_list

        out["environments"] = capo_finspace.types.environment_list.serialize_json(
            value["environments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if "environments" in data:
        import capo_finspace.types.environment_list

        out["environments"] = capo_finspace.types.environment_list.deserialize_json(
            data["environments"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
