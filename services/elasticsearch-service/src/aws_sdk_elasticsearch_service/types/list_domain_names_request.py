"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListDomainNamesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.engine_type


class ListDomainNamesRequest(TypedDict):
    engine_type: NotRequired[
        "aws_sdk_elasticsearch_service.types.engine_type.EngineType"
    ]
    """<p> Optional parameter to filter the output by domain engine type. Acceptable values are 'Elasticsearch' and 'OpenSearch'. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainNamesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainNamesRequest:
    out: ListDomainNamesRequest = {}  # type: ignore[typeddict-item]
    return out
