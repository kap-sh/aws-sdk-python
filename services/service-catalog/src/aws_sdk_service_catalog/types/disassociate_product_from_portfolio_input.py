"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateProductFromPortfolioInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id


class DisassociateProductFromPortfolioInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    portfolio_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateProductFromPortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    out["PortfolioId"] = value["portfolio_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateProductFromPortfolioInput:
    out: DisassociateProductFromPortfolioInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "DisassociateProductFromPortfolioInput.product_id required"
        )
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError(
            "DisassociateProductFromPortfolioInput.portfolio_id required"
        )
    return out
