"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDryRunProgressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_status
    import aws_sdk_opensearch.types.dry_run_progress_status
    import aws_sdk_opensearch.types.dry_run_results


class DescribeDryRunProgressResponse(TypedDict, closed=True):
    dry_run_progress_status: NotRequired[
        "aws_sdk_opensearch.types.dry_run_progress_status.DryRunProgressStatus"
    ]
    """<p>The current status of the dry run, including any validation errors.</p>"""
    dry_run_config: NotRequired["aws_sdk_opensearch.types.domain_status.DomainStatus"]
    """<p>Details about the changes you're planning to make on the domain.</p>"""
    dry_run_results: NotRequired[
        "aws_sdk_opensearch.types.dry_run_results.DryRunResults"
    ]
    """<p>The results of the dry run. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDryRunProgressResponse) -> dict:
    out: dict = {}
    if "dry_run_progress_status" in value:
        import aws_sdk_opensearch.types.dry_run_progress_status

        out["DryRunProgressStatus"] = (
            aws_sdk_opensearch.types.dry_run_progress_status.serialize_json(
                value["dry_run_progress_status"]
            )
        )
    if "dry_run_config" in value:
        import aws_sdk_opensearch.types.domain_status

        out["DryRunConfig"] = aws_sdk_opensearch.types.domain_status.serialize_json(
            value["dry_run_config"]
        )
    if "dry_run_results" in value:
        import aws_sdk_opensearch.types.dry_run_results

        out["DryRunResults"] = aws_sdk_opensearch.types.dry_run_results.serialize_json(
            value["dry_run_results"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDryRunProgressResponse:
    out: DescribeDryRunProgressResponse = {}  # type: ignore[typeddict-item]
    if "DryRunProgressStatus" in data:
        import aws_sdk_opensearch.types.dry_run_progress_status

        out["dry_run_progress_status"] = (
            aws_sdk_opensearch.types.dry_run_progress_status.deserialize_json(
                data["DryRunProgressStatus"]
            )
        )
    if "DryRunConfig" in data:
        import aws_sdk_opensearch.types.domain_status

        out["dry_run_config"] = aws_sdk_opensearch.types.domain_status.deserialize_json(
            data["DryRunConfig"]
        )
    if "DryRunResults" in data:
        import aws_sdk_opensearch.types.dry_run_results

        out["dry_run_results"] = (
            aws_sdk_opensearch.types.dry_run_results.deserialize_json(
                data["DryRunResults"]
            )
        )
    return out
