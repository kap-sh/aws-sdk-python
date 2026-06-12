"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainLogPublishingOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config


class AwsElasticsearchDomainLogPublishingOptions(TypedDict):
    index_slow_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.AwsElasticsearchDomainLogPublishingOptionsLogConfig"
    ]
    """<p>Configures the OpenSearch index logs publishing.</p>"""
    search_slow_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.AwsElasticsearchDomainLogPublishingOptionsLogConfig"
    ]
    """<p>Configures the OpenSearch search slow log publishing.</p>"""
    audit_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.AwsElasticsearchDomainLogPublishingOptionsLogConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainLogPublishingOptions) -> dict:
    out: dict = {}
    if "index_slow_logs" in value:
        import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config

        out["IndexSlowLogs"] = (
            aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.serialize_json(
                value["index_slow_logs"]
            )
        )
    if "search_slow_logs" in value:
        import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config

        out["SearchSlowLogs"] = (
            aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.serialize_json(
                value["search_slow_logs"]
            )
        )
    if "audit_logs" in value:
        import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config

        out["AuditLogs"] = (
            aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainLogPublishingOptions:
    out: AwsElasticsearchDomainLogPublishingOptions = {}  # type: ignore[typeddict-item]
    if "IndexSlowLogs" in data:
        import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config

        out["index_slow_logs"] = (
            aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.deserialize_json(
                data["IndexSlowLogs"]
            )
        )
    if "SearchSlowLogs" in data:
        import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config

        out["search_slow_logs"] = (
            aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.deserialize_json(
                data["SearchSlowLogs"]
            )
        )
    if "AuditLogs" in data:
        import aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config

        out["audit_logs"] = (
            aws_sdk_securityhub.types.aws_elasticsearch_domain_log_publishing_options_log_config.deserialize_json(
                data["AuditLogs"]
            )
        )
    return out
