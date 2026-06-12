"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListSegmentDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size500
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token


class ListSegmentDefinitionsRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique identifier of the domain.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size500.MaxSize500"]
    """<p>The maximum number of objects returned per page.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSegmentDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSegmentDefinitionsRequest:
    out: ListSegmentDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
