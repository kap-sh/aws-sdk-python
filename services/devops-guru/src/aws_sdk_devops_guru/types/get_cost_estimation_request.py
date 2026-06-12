"""Generated from Smithy shape ``com.amazonaws.devopsguru#GetCostEstimationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.uuid_next_token


class GetCostEstimationRequest(TypedDict):
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCostEstimationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCostEstimationRequest:
    out: GetCostEstimationRequest = {}  # type: ignore[typeddict-item]
    return out
