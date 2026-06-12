"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDomainNamesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.engine_type


class ListDomainNamesRequest(TypedDict):
    engine_type: NotRequired["aws_sdk_opensearch.types.engine_type.EngineType"]
    """<p>Filters the output by domain engine type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainNamesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainNamesRequest:
    out: ListDomainNamesRequest = {}  # type: ignore[typeddict-item]
    return out
