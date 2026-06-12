"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetCompatibleElasticsearchVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name


class GetCompatibleElasticsearchVersionsRequest(TypedDict):
    domain_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleElasticsearchVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCompatibleElasticsearchVersionsRequest:
    out: GetCompatibleElasticsearchVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
