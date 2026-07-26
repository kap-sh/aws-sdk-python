"""Generated from Smithy shape ``com.amazonaws.inspector2#RepositoryAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts


class RepositoryAggregationResponse(TypedDict, closed=True):
    repository: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The name of the repository associated with the findings.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the findings.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that represent the count of matched findings per severity.</p>"""
    affected_images: NotRequired["int"]
    """<p>The number of container images impacted by the findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAggregationResponse) -> dict:
    out: dict = {}
    out["repository"] = value["repository"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "affected_images" in value:
        out["affectedImages"] = value["affected_images"]
    return out


def deserialize_json(data: dict) -> RepositoryAggregationResponse:
    out: RepositoryAggregationResponse = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        out["repository"] = data["repository"]
    else:
        raise DeserializationError("RepositoryAggregationResponse.repository required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if "affectedImages" in data:
        out["affected_images"] = data["affectedImages"]
    return out
