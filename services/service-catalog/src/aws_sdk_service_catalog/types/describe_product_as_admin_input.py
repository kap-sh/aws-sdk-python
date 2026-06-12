"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProductAsAdminInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.product_view_name


class DescribeProductAsAdminInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    name: NotRequired["aws_sdk_service_catalog.types.product_view_name.ProductViewName"]
    """<p>The product name.</p>"""
    source_portfolio_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The unique identifier of the shared portfolio that the specified product is associated with.</p> <p>You can provide this parameter to retrieve the shared TagOptions associated with the product. If this parameter is provided and if TagOptions sharing is enabled in the portfolio share, the API returns both local and shared TagOptions associated with the product. Otherwise only local TagOptions will be returned. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProductAsAdminInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "source_portfolio_id" in value:
        out["SourcePortfolioId"] = value["source_portfolio_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProductAsAdminInput:
    out: DescribeProductAsAdminInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SourcePortfolioId" in data:
        out["source_portfolio_id"] = data["SourcePortfolioId"]
    return out
