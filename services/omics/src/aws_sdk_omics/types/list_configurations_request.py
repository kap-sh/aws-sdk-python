"""Generated from Smithy shape ``com.amazonaws.omics#ListConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.configuration_list_token


class ListConfigurationsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return.</p>"""
    starting_token: NotRequired[
        "aws_sdk_omics.types.configuration_list_token.ConfigurationListToken"
    ]
    """<p>Pagination token for retrieving next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConfigurationsRequest:
    out: ListConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
