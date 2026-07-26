"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListPortfolioAccessInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.page_size_max100
    import capo_service_catalog.types.page_token


class ListPortfolioAccessInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    organization_parent_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The ID of an organization node the portfolio is shared with. All children of this node with an inherited portfolio share will be returned.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    page_size: "capo_service_catalog.types.page_size_max100.PageSizeMax100"
    """<p>The maximum number of items to return with this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPortfolioAccessInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    if "organization_parent_id" in value:
        out["OrganizationParentId"] = value["organization_parent_id"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    out["PageSize"] = value.get("page_size", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPortfolioAccessInput:
    out: ListPortfolioAccessInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("ListPortfolioAccessInput.portfolio_id required")
    if "OrganizationParentId" in data:
        out["organization_parent_id"] = data["OrganizationParentId"]
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    return out
