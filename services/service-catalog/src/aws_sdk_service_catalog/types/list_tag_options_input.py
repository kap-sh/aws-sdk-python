"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListTagOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.list_tag_options_filters
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token


class ListTagOptionsInput(TypedDict):
    filters: NotRequired[
        "aws_sdk_service_catalog.types.list_tag_options_filters.ListTagOptionsFilters"
    ]
    """<p>The search filters. If no search filters are specified, the output includes all TagOptions.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagOptionsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_service_catalog.types.list_tag_options_filters

        out["Filters"] = (
            aws_sdk_service_catalog.types.list_tag_options_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagOptionsInput:
    out: ListTagOptionsInput = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_service_catalog.types.list_tag_options_filters

        out["filters"] = (
            aws_sdk_service_catalog.types.list_tag_options_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
