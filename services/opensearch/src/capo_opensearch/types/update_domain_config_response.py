"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDomainConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.domain_config
    import capo_opensearch.types.dry_run_progress_status
    import capo_opensearch.types.dry_run_results


class UpdateDomainConfigResponse(TypedDict, closed=True):
    domain_config: "capo_opensearch.types.domain_config.DomainConfig"
    """<p>The status of the updated domain.</p>"""
    dry_run_results: NotRequired["capo_opensearch.types.dry_run_results.DryRunResults"]
    """<p>Results of the dry run performed in the update domain request.</p>"""
    dry_run_progress_status: NotRequired[
        "capo_opensearch.types.dry_run_progress_status.DryRunProgressStatus"
    ]
    """<p>The status of the dry run being performed on the domain, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainConfigResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.domain_config

    out["DomainConfig"] = capo_opensearch.types.domain_config.serialize_json(
        value["domain_config"]
    )
    if "dry_run_results" in value:
        import capo_opensearch.types.dry_run_results

        out["DryRunResults"] = capo_opensearch.types.dry_run_results.serialize_json(
            value["dry_run_results"]
        )
    if "dry_run_progress_status" in value:
        import capo_opensearch.types.dry_run_progress_status

        out["DryRunProgressStatus"] = (
            capo_opensearch.types.dry_run_progress_status.serialize_json(
                value["dry_run_progress_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDomainConfigResponse:
    out: UpdateDomainConfigResponse = {}  # type: ignore[typeddict-item]
    if "DomainConfig" in data:
        import capo_opensearch.types.domain_config

        out["domain_config"] = capo_opensearch.types.domain_config.deserialize_json(
            data["DomainConfig"]
        )
    else:
        raise DeserializationError("UpdateDomainConfigResponse.domain_config required")
    if "DryRunResults" in data:
        import capo_opensearch.types.dry_run_results

        out["dry_run_results"] = capo_opensearch.types.dry_run_results.deserialize_json(
            data["DryRunResults"]
        )
    if "DryRunProgressStatus" in data:
        import capo_opensearch.types.dry_run_progress_status

        out["dry_run_progress_status"] = (
            capo_opensearch.types.dry_run_progress_status.deserialize_json(
                data["DryRunProgressStatus"]
            )
        )
    return out
