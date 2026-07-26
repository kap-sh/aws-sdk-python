"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageScanFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_scan_findings_filter_list
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListImageScanFindingsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_imagebuilder.types.image_scan_findings_filter_list.ImageScanFindingsFilterList"
    ]
    """<p>An array of name value pairs that you can use to filter your results. You can use the following filters to streamline results:</p> <ul> <li> <p> <code>imageBuildVersionArn</code> </p> </li> <li> <p> <code>imagePipelineArn</code> </p> </li> <li> <p> <code>vulnerabilityId</code> </p> </li> <li> <p> <code>severity</code> </p> </li> </ul> <p>If you don't request a filter, then all findings in your account are listed.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageScanFindingsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_imagebuilder.types.image_scan_findings_filter_list

        out["filters"] = (
            capo_imagebuilder.types.image_scan_findings_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageScanFindingsRequest:
    out: ListImageScanFindingsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_imagebuilder.types.image_scan_findings_filter_list

        out["filters"] = (
            capo_imagebuilder.types.image_scan_findings_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
