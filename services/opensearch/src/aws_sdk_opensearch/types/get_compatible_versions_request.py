"""Generated from Smithy shape ``com.amazonaws.opensearch#GetCompatibleVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name


class GetCompatibleVersionsRequest(TypedDict):
    domain_name: NotRequired["aws_sdk_opensearch.types.domain_name.DomainName"]
    """<p>The name of an existing domain. Provide this parameter to limit the results to a single domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCompatibleVersionsRequest:
    out: GetCompatibleVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
