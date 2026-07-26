"""Generated from Smithy shape ``com.amazonaws.appsync#GetGraphqlApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class GetGraphqlApiRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID for the GraphQL API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphqlApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphqlApiRequest:
    out: GetGraphqlApiRequest = {}  # type: ignore[typeddict-item]
    return out
