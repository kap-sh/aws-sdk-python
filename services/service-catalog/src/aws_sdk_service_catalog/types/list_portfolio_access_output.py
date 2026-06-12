"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListPortfolioAccessOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.account_ids
    import aws_sdk_service_catalog.types.page_token


class ListPortfolioAccessOutput(TypedDict):
    account_ids: NotRequired["aws_sdk_service_catalog.types.account_ids.AccountIds"]
    """<p>Information about the Amazon Web Services accounts with access to the portfolio.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPortfolioAccessOutput) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_service_catalog.types.account_ids

        out["AccountIds"] = (
            aws_sdk_service_catalog.types.account_ids.serialize_aws_json_1_1(
                value["account_ids"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPortfolioAccessOutput:
    out: ListPortfolioAccessOutput = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_service_catalog.types.account_ids

        out["account_ids"] = (
            aws_sdk_service_catalog.types.account_ids.deserialize_aws_json_1_1(
                data["AccountIds"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
