"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListEventStreamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token


class ListEventStreamsRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventStreamsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventStreamsRequest:
    out: ListEventStreamsRequest = {}  # type: ignore[typeddict-item]
    return out
