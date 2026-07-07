"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListIdentityPoolUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.integer_string
    import aws_sdk_cognito_sync.types.string


class ListIdentityPoolUsageRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cognito_sync.types.string.String"]
    """A pagination token for obtaining the next page of results."""
    max_results: NotRequired["aws_sdk_cognito_sync.types.integer_string.IntegerString"]
    """The maximum number of results to be returned."""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityPoolUsageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentityPoolUsageRequest:
    out: ListIdentityPoolUsageRequest = {}  # type: ignore[typeddict-item]
    return out
