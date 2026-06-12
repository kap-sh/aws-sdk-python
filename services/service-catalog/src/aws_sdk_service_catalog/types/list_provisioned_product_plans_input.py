"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisionedProductPlansInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.access_level_filter
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token


class ListProvisionedProductPlansInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provision_product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    access_level_filter: NotRequired[
        "aws_sdk_service_catalog.types.access_level_filter.AccessLevelFilter"
    ]
    """<p>The access level to use to obtain results. The default is <code>User</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProvisionedProductPlansInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "provision_product_id" in value:
        out["ProvisionProductId"] = value["provision_product_id"]
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "access_level_filter" in value:
        import aws_sdk_service_catalog.types.access_level_filter

        out["AccessLevelFilter"] = (
            aws_sdk_service_catalog.types.access_level_filter.serialize_aws_json_1_1(
                value["access_level_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProvisionedProductPlansInput:
    out: ListProvisionedProductPlansInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProvisionProductId" in data:
        out["provision_product_id"] = data["ProvisionProductId"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    if "AccessLevelFilter" in data:
        import aws_sdk_service_catalog.types.access_level_filter

        out["access_level_filter"] = (
            aws_sdk_service_catalog.types.access_level_filter.deserialize_aws_json_1_1(
                data["AccessLevelFilter"]
            )
        )
    return out
