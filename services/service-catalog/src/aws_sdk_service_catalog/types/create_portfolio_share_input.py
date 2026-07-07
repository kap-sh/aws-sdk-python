"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreatePortfolioShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.account_id
    import aws_sdk_service_catalog.types.boolean
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.organization_node


class CreatePortfolioShareInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    account_id: NotRequired["aws_sdk_service_catalog.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID. For example, <code>123456789012</code>.</p>"""
    organization_node: NotRequired[
        "aws_sdk_service_catalog.types.organization_node.OrganizationNode"
    ]
    """<p>The organization node to whom you are going to share. When you pass <code>OrganizationNode</code>, it creates <code>PortfolioShare</code> for all of the Amazon Web Services accounts that are associated to the <code>OrganizationNode</code>. The output returns a <code>PortfolioShareToken</code>, which enables the administrator to monitor the status of the <code>PortfolioShare</code> creation process.</p>"""
    share_tag_options: "aws_sdk_service_catalog.types.boolean.Boolean"
    """<p>Enables or disables <code>TagOptions </code> sharing when creating the portfolio share. If this flag is not provided, TagOptions sharing is disabled.</p>"""
    share_principals: "aws_sdk_service_catalog.types.boolean.Boolean"
    """<p>This parameter is only supported for portfolios with an <b>OrganizationalNode</b> Type of <code>ORGANIZATION</code> or <code>ORGANIZATIONAL_UNIT</code>. </p> <p>Enables or disables <code>Principal</code> sharing when creating the portfolio share. If you do <b>not</b> provide this flag, principal sharing is disabled. </p> <p>When you enable Principal Name Sharing for a portfolio share, the share recipient account end users with a principal that matches any of the associated IAM patterns can provision products from the portfolio. Once shared, the share recipient can view associations of <code>PrincipalType</code>: <code>IAM_PATTERN</code> on their portfolio. You can create the principals in the recipient account before or after creating the share. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePortfolioShareInput) -> dict:
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
    out["ShareTagOptions"] = value.get("share_tag_options", False)
    out["SharePrincipals"] = value.get("share_principals", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePortfolioShareInput:
    out: CreatePortfolioShareInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("CreatePortfolioShareInput.portfolio_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "OrganizationNode" in data:
        import aws_sdk_service_catalog.types.organization_node

        out["organization_node"] = (
            aws_sdk_service_catalog.types.organization_node.deserialize_aws_json_1_1(
                data["OrganizationNode"]
            )
        )
    if "ShareTagOptions" in data:
        out["share_tag_options"] = data["ShareTagOptions"]
    else:
        out["share_tag_options"] = False
    if "SharePrincipals" in data:
        out["share_principals"] = data["SharePrincipals"]
    else:
        out["share_principals"] = False
    return out
