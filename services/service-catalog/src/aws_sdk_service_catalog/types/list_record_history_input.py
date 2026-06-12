"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListRecordHistoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.access_level_filter
    import aws_sdk_service_catalog.types.list_record_history_search_filter
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token


class ListRecordHistoryInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    access_level_filter: NotRequired[
        "aws_sdk_service_catalog.types.access_level_filter.AccessLevelFilter"
    ]
    """<p>The access level to use to obtain results. The default is <code>User</code>.</p>"""
    search_filter: NotRequired[
        "aws_sdk_service_catalog.types.list_record_history_search_filter.ListRecordHistorySearchFilter"
    ]
    """<p>The search filter to scope the results.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecordHistoryInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "access_level_filter" in value:
        import aws_sdk_service_catalog.types.access_level_filter

        out["AccessLevelFilter"] = (
            aws_sdk_service_catalog.types.access_level_filter.serialize_aws_json_1_1(
                value["access_level_filter"]
            )
        )
    if "search_filter" in value:
        import aws_sdk_service_catalog.types.list_record_history_search_filter

        out["SearchFilter"] = (
            aws_sdk_service_catalog.types.list_record_history_search_filter.serialize_aws_json_1_1(
                value["search_filter"]
            )
        )
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecordHistoryInput:
    out: ListRecordHistoryInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "AccessLevelFilter" in data:
        import aws_sdk_service_catalog.types.access_level_filter

        out["access_level_filter"] = (
            aws_sdk_service_catalog.types.access_level_filter.deserialize_aws_json_1_1(
                data["AccessLevelFilter"]
            )
        )
    if "SearchFilter" in data:
        import aws_sdk_service_catalog.types.list_record_history_search_filter

        out["search_filter"] = (
            aws_sdk_service_catalog.types.list_record_history_search_filter.deserialize_aws_json_1_1(
                data["SearchFilter"]
            )
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
