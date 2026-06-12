"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListBudgetsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.budgets
    import aws_sdk_service_catalog.types.page_token


class ListBudgetsForResourceOutput(TypedDict):
    budgets: NotRequired["aws_sdk_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBudgetsForResourceOutput) -> dict:
    out: dict = {}
    if "budgets" in value:
        import aws_sdk_service_catalog.types.budgets

        out["Budgets"] = aws_sdk_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBudgetsForResourceOutput:
    out: ListBudgetsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Budgets" in data:
        import aws_sdk_service_catalog.types.budgets

        out["budgets"] = aws_sdk_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
