"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListLoaderJobsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.positive_integer


class ListLoaderJobsInput(TypedDict):
    limit: NotRequired["aws_sdk_neptunedata.types.positive_integer.PositiveInteger"]
    """<p>The number of load IDs to list. Must be a positive integer greater than zero and not more than <code>100</code> (which is the default).</p>"""
    include_queued_loads: NotRequired["bool"]
    """<p>An optional parameter that can be used to exclude the load IDs of queued load requests when requesting a list of load IDs by setting the parameter to <code>FALSE</code>. The default value is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoaderJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLoaderJobsInput:
    out: ListLoaderJobsInput = {}  # type: ignore[typeddict-item]
    return out
