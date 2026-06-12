"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_domain_config


class DescribeElasticsearchDomainConfigResponse(TypedDict):
    domain_config: "aws_sdk_elasticsearch_service.types.elasticsearch_domain_config.ElasticsearchDomainConfig"
    """<p>The configuration information of the domain requested in the <code>DescribeElasticsearchDomainConfig</code> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainConfigResponse) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.elasticsearch_domain_config

    out["DomainConfig"] = (
        aws_sdk_elasticsearch_service.types.elasticsearch_domain_config.serialize_json(
            value["domain_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainConfigResponse:
    out: DescribeElasticsearchDomainConfigResponse = {}  # type: ignore[typeddict-item]
    if "DomainConfig" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_domain_config

        out["domain_config"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_domain_config.deserialize_json(
                data["DomainConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeElasticsearchDomainConfigResponse.domain_config required"
        )
    return out
