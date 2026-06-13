"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListControlMappingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_mapping_filter
    import aws_sdk_controlcatalog.types.max_list_control_mappings_results
    import aws_sdk_controlcatalog.types.pagination_token


class ListControlMappingsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_controlcatalog.types.max_list_control_mappings_results.MaxListControlMappingsResults"
    ]
    """<p>The maximum number of results on a page or for an API request call.</p>"""
    filter: NotRequired[
        "aws_sdk_controlcatalog.types.control_mapping_filter.ControlMappingFilter"
    ]
    """<p>An optional filter that narrows the results to specific control mappings based on control ARNs, common control ARNs, or mapping types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlMappingsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_controlcatalog.types.control_mapping_filter

        out["Filter"] = (
            aws_sdk_controlcatalog.types.control_mapping_filter.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListControlMappingsRequest:
    out: ListControlMappingsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_controlcatalog.types.control_mapping_filter

        out["filter"] = (
            aws_sdk_controlcatalog.types.control_mapping_filter.deserialize_json(
                data["Filter"]
            )
        )
    return out
