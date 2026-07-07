"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#ListSuiteDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.max_results
    import aws_sdk_iotdeviceadvisor.types.token


class ListSuiteDefinitionsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_iotdeviceadvisor.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at once.</p>"""
    next_token: NotRequired["aws_sdk_iotdeviceadvisor.types.token.Token"]
    """<p>A token used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuiteDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSuiteDefinitionsRequest:
    out: ListSuiteDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
