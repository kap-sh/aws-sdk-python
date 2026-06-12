"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDomainConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_config
    import aws_sdk_opensearch.types.dry_run_progress_status
    import aws_sdk_opensearch.types.dry_run_results


class UpdateDomainConfigResponse(TypedDict):
    domain_config: "aws_sdk_opensearch.types.domain_config.DomainConfig"
    """<p>The status of the updated domain.</p>"""
    dry_run_results: NotRequired[
        "aws_sdk_opensearch.types.dry_run_results.DryRunResults"
    ]
    """<p>Results of the dry run performed in the update domain request.</p>"""
    dry_run_progress_status: NotRequired[
        "aws_sdk_opensearch.types.dry_run_progress_status.DryRunProgressStatus"
    ]
    """<p>The status of the dry run being performed on the domain, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainConfigResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.domain_config

    out["DomainConfig"] = aws_sdk_opensearch.types.domain_config.serialize_json(
        value["domain_config"]
    )
    if "dry_run_results" in value:
        import aws_sdk_opensearch.types.dry_run_results

        out["DryRunResults"] = aws_sdk_opensearch.types.dry_run_results.serialize_json(
            value["dry_run_results"]
        )
    if "dry_run_progress_status" in value:
        import aws_sdk_opensearch.types.dry_run_progress_status

        out["DryRunProgressStatus"] = (
            aws_sdk_opensearch.types.dry_run_progress_status.serialize_json(
                value["dry_run_progress_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDomainConfigResponse:
    out: UpdateDomainConfigResponse = {}  # type: ignore[typeddict-item]
    if "DomainConfig" in data:
        import aws_sdk_opensearch.types.domain_config

        out["domain_config"] = aws_sdk_opensearch.types.domain_config.deserialize_json(
            data["DomainConfig"]
        )
    else:
        raise DeserializationError("UpdateDomainConfigResponse.domain_config required")
    if "DryRunResults" in data:
        import aws_sdk_opensearch.types.dry_run_results

        out["dry_run_results"] = (
            aws_sdk_opensearch.types.dry_run_results.deserialize_json(
                data["DryRunResults"]
            )
        )
    if "DryRunProgressStatus" in data:
        import aws_sdk_opensearch.types.dry_run_progress_status

        out["dry_run_progress_status"] = (
            aws_sdk_opensearch.types.dry_run_progress_status.deserialize_json(
                data["DryRunProgressStatus"]
            )
        )
    return out
