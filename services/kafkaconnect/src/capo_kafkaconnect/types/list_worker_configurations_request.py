"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListWorkerConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.max_results


class ListWorkerConfigurationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_kafkaconnect.types.max_results.MaxResults"]
    """<p>The maximum number of worker configurations to list in one response.</p>"""
    next_token: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>If the response of a ListWorkerConfigurations operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>"""
    name_prefix: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>Lists worker configuration names that start with the specified text string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkerConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkerConfigurationsRequest:
    out: ListWorkerConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
