"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListCustomPluginsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.max_results


class ListCustomPluginsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_kafkaconnect.types.max_results.MaxResults"]
    """<p>The maximum number of custom plugins to list in one response.</p>"""
    next_token: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>If the response of a ListCustomPlugins operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.</p>"""
    name_prefix: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>Lists custom plugin names that start with the specified text string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomPluginsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomPluginsRequest:
    out: ListCustomPluginsRequest = {}  # type: ignore[typeddict-item]
    return out
