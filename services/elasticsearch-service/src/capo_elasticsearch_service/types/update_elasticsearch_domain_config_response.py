"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdateElasticsearchDomainConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.dry_run_results
    import capo_elasticsearch_service.types.elasticsearch_domain_config


class UpdateElasticsearchDomainConfigResponse(TypedDict, closed=True):
    domain_config: "capo_elasticsearch_service.types.elasticsearch_domain_config.ElasticsearchDomainConfig"
    """<p>The status of the updated Elasticsearch domain. </p>"""
    dry_run_results: NotRequired[
        "capo_elasticsearch_service.types.dry_run_results.DryRunResults"
    ]
    """<p>Contains result of DryRun. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateElasticsearchDomainConfigResponse) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.elasticsearch_domain_config

    out["DomainConfig"] = (
        capo_elasticsearch_service.types.elasticsearch_domain_config.serialize_json(
            value["domain_config"]
        )
    )
    if "dry_run_results" in value:
        import capo_elasticsearch_service.types.dry_run_results

        out["DryRunResults"] = (
            capo_elasticsearch_service.types.dry_run_results.serialize_json(
                value["dry_run_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateElasticsearchDomainConfigResponse:
    out: UpdateElasticsearchDomainConfigResponse = {}  # type: ignore[typeddict-item]
    if "DomainConfig" in data:
        import capo_elasticsearch_service.types.elasticsearch_domain_config

        out["domain_config"] = (
            capo_elasticsearch_service.types.elasticsearch_domain_config.deserialize_json(
                data["DomainConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateElasticsearchDomainConfigResponse.domain_config required"
        )
    if "DryRunResults" in data:
        import capo_elasticsearch_service.types.dry_run_results

        out["dry_run_results"] = (
            capo_elasticsearch_service.types.dry_run_results.deserialize_json(
                data["DryRunResults"]
            )
        )
    return out
