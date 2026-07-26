"""Generated from Smithy shape ``com.amazonaws.iot#ListSbomValidationResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.package_catalog_max_results
    import capo_iot.types.package_name
    import capo_iot.types.sbom_validation_result
    import capo_iot.types.version_name


class ListSbomValidationResultsRequest(TypedDict, closed=True):
    package_name: "capo_iot.types.package_name.PackageName"
    """<p>The name of the new software package.</p>"""
    version_name: "capo_iot.types.version_name.VersionName"
    """<p>The name of the new package version.</p>"""
    validation_result: NotRequired[
        "capo_iot.types.sbom_validation_result.SbomValidationResult"
    ]
    """<p>The end result of the </p>"""
    max_results: NotRequired[
        "capo_iot.types.package_catalog_max_results.PackageCatalogMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSbomValidationResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSbomValidationResultsRequest:
    out: ListSbomValidationResultsRequest = {}  # type: ignore[typeddict-item]
    return out
