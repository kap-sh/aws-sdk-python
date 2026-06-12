"""Generated from Smithy shape ``com.amazonaws.appsync#GetGraphqlApiRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class GetGraphqlApiRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID for the GraphQL API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphqlApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphqlApiRequest:
    out: GetGraphqlApiRequest = {}  # type: ignore[typeddict-item]
    return out
