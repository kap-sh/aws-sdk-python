"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name_list


class DescribeElasticsearchDomainsRequest(TypedDict):
    domain_names: "aws_sdk_elasticsearch_service.types.domain_name_list.DomainNameList"
    """<p>The Elasticsearch domains for which you want information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainsRequest) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.domain_name_list

    out["DomainNames"] = (
        aws_sdk_elasticsearch_service.types.domain_name_list.serialize_json(
            value["domain_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainsRequest:
    out: DescribeElasticsearchDomainsRequest = {}  # type: ignore[typeddict-item]
    if "DomainNames" in data:
        import aws_sdk_elasticsearch_service.types.domain_name_list

        out["domain_names"] = (
            aws_sdk_elasticsearch_service.types.domain_name_list.deserialize_json(
                data["DomainNames"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeElasticsearchDomainsRequest.domain_names required"
        )
    return out
