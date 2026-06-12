"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeletePortfolioShareInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.account_id
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.organization_node


class DeletePortfolioShareInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    account_id: NotRequired["aws_sdk_service_catalog.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    organization_node: NotRequired[
        "aws_sdk_service_catalog.types.organization_node.OrganizationNode"
    ]
    """<p>The organization node to whom you are going to stop sharing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePortfolioShareInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "organization_node" in value:
        import aws_sdk_service_catalog.types.organization_node

        out["OrganizationNode"] = (
            aws_sdk_service_catalog.types.organization_node.serialize_aws_json_1_1(
                value["organization_node"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePortfolioShareInput:
    out: DeletePortfolioShareInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("DeletePortfolioShareInput.portfolio_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "OrganizationNode" in data:
        import aws_sdk_service_catalog.types.organization_node

        out["organization_node"] = (
            aws_sdk_service_catalog.types.organization_node.deserialize_aws_json_1_1(
                data["OrganizationNode"]
            )
        )
    return out
