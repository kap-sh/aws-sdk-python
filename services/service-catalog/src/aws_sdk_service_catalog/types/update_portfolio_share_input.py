"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatePortfolioShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.account_id
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.nullable_boolean
    import aws_sdk_service_catalog.types.organization_node


class UpdatePortfolioShareInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The unique identifier of the portfolio for which the share will be updated.</p>"""
    account_id: NotRequired["aws_sdk_service_catalog.types.account_id.AccountId"]
    """<p>The Amazon Web Services account Id of the recipient account. This field is required when updating an external account to account type share.</p>"""
    organization_node: NotRequired[
        "aws_sdk_service_catalog.types.organization_node.OrganizationNode"
    ]
    share_tag_options: NotRequired[
        "aws_sdk_service_catalog.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables or disables <code>TagOptions</code> sharing for the portfolio share. If this field is not provided, the current state of TagOptions sharing on the portfolio share will not be modified.</p>"""
    share_principals: NotRequired[
        "aws_sdk_service_catalog.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A flag to enables or disables <code>Principals</code> sharing in the portfolio. If this field is not provided, the current state of the <code>Principals</code> sharing on the portfolio share will not be modified. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePortfolioShareInput) -> dict:
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
    if "share_tag_options" in value:
        out["ShareTagOptions"] = value["share_tag_options"]
    if "share_principals" in value:
        out["SharePrincipals"] = value["share_principals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePortfolioShareInput:
    out: UpdatePortfolioShareInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("UpdatePortfolioShareInput.portfolio_id required")
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
    if "SharePrincipals" in data:
        out["share_principals"] = data["SharePrincipals"]
    return out
