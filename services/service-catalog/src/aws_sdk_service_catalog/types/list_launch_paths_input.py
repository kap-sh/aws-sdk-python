"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListLaunchPathsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token


class ListLaunchPathsInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLaunchPathsInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLaunchPathsInput:
    out: ListLaunchPathsInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError("ListLaunchPathsInput.product_id required")
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
