"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PortfolioShareDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.boolean
    import aws_sdk_service_catalog.types.describe_portfolio_share_type
    import aws_sdk_service_catalog.types.id


class PortfolioShareDetail(TypedDict):
    principal_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the recipient entity that received the portfolio share. The recipient entity can be one of the following:</p> <p>1. An external account.</p> <p>2. An organziation member account.</p> <p>3. An organzational unit (OU).</p> <p>4. The organization itself. (This shares with every account in the organization).</p>"""
    type: NotRequired[
        "aws_sdk_service_catalog.types.describe_portfolio_share_type.DescribePortfolioShareType"
    ]
    """<p>The type of the portfolio share.</p>"""
    accepted: "aws_sdk_service_catalog.types.boolean.Boolean"
    """<p>Indicates whether the shared portfolio is imported by the recipient account. If the recipient is in an organization node, the share is automatically imported, and the field is always set to true.</p>"""
    share_tag_options: "aws_sdk_service_catalog.types.boolean.Boolean"
    """<p>Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.</p>"""
    share_principals: "aws_sdk_service_catalog.types.boolean.Boolean"
    """<p>Indicates if <code>Principal</code> sharing is enabled or disabled for the portfolio share. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortfolioShareDetail) -> dict:
    out: dict = {}
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "type" in value:
        import aws_sdk_service_catalog.types.describe_portfolio_share_type

        out["Type"] = (
            aws_sdk_service_catalog.types.describe_portfolio_share_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    out["Accepted"] = value.get("accepted", False)
    out["ShareTagOptions"] = value.get("share_tag_options", False)
    out["SharePrincipals"] = value.get("share_principals", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PortfolioShareDetail:
    out: PortfolioShareDetail = {}  # type: ignore[typeddict-item]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "Type" in data:
        import aws_sdk_service_catalog.types.describe_portfolio_share_type

        out["type"] = (
            aws_sdk_service_catalog.types.describe_portfolio_share_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Accepted" in data:
        out["accepted"] = data["Accepted"]
    else:
        out["accepted"] = False
    if "ShareTagOptions" in data:
        out["share_tag_options"] = data["ShareTagOptions"]
    else:
        out["share_tag_options"] = False
    if "SharePrincipals" in data:
        out["share_principals"] = data["SharePrincipals"]
    else:
        out["share_principals"] = False
    return out
