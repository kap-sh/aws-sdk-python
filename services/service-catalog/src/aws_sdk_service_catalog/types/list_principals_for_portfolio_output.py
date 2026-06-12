"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListPrincipalsForPortfolioOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.principals


class ListPrincipalsForPortfolioOutput(TypedDict):
    principals: NotRequired["aws_sdk_service_catalog.types.principals.Principals"]
    """<p>The <code>PrincipalARN</code>s and corresponding <code>PrincipalType</code>s associated with the portfolio.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPrincipalsForPortfolioOutput) -> dict:
    out: dict = {}
    if "principals" in value:
        import aws_sdk_service_catalog.types.principals

        out["Principals"] = (
            aws_sdk_service_catalog.types.principals.serialize_aws_json_1_1(
                value["principals"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPrincipalsForPortfolioOutput:
    out: ListPrincipalsForPortfolioOutput = {}  # type: ignore[typeddict-item]
    if "Principals" in data:
        import aws_sdk_service_catalog.types.principals

        out["principals"] = (
            aws_sdk_service_catalog.types.principals.deserialize_aws_json_1_1(
                data["Principals"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
