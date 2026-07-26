"""Generated from Smithy shape ``com.amazonaws.kafka#ListScramSecretsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.max_results


class ListScramSecretsRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The arn of the cluster.</p>"""
    max_results: NotRequired["capo_kafka.types.max_results.MaxResults"]
    """<p>The maxResults of the query.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The nextToken of the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScramSecretsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScramSecretsRequest:
    out: ListScramSecretsRequest = {}  # type: ignore[typeddict-item]
    return out
