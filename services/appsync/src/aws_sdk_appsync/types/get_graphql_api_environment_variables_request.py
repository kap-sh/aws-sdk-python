"""Generated from Smithy shape ``com.amazonaws.appsync#GetGraphqlApiEnvironmentVariablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class GetGraphqlApiEnvironmentVariablesRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The ID of the API from which the environmental variable list will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphqlApiEnvironmentVariablesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphqlApiEnvironmentVariablesRequest:
    out: GetGraphqlApiEnvironmentVariablesRequest = {}  # type: ignore[typeddict-item]
    return out
