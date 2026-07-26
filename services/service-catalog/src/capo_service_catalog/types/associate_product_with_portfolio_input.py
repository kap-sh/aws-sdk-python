"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateProductWithPortfolioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id


class AssociateProductWithPortfolioInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    source_portfolio_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the source portfolio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateProductWithPortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    out["PortfolioId"] = value["portfolio_id"]
    if "source_portfolio_id" in value:
        out["SourcePortfolioId"] = value["source_portfolio_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateProductWithPortfolioInput:
    out: AssociateProductWithPortfolioInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "AssociateProductWithPortfolioInput.product_id required"
        )
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError(
            "AssociateProductWithPortfolioInput.portfolio_id required"
        )
    if "SourcePortfolioId" in data:
        out["source_portfolio_id"] = data["SourcePortfolioId"]
    return out
