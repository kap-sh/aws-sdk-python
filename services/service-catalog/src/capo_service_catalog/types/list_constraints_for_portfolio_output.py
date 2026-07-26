"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListConstraintsForPortfolioOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.constraint_details
    import capo_service_catalog.types.page_token


class ListConstraintsForPortfolioOutput(TypedDict, closed=True):
    constraint_details: NotRequired[
        "capo_service_catalog.types.constraint_details.ConstraintDetails"
    ]
    """<p>Information about the constraints.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConstraintsForPortfolioOutput) -> dict:
    out: dict = {}
    if "constraint_details" in value:
        import capo_service_catalog.types.constraint_details

        out["ConstraintDetails"] = (
            capo_service_catalog.types.constraint_details.serialize_aws_json_1_1(
                value["constraint_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConstraintsForPortfolioOutput:
    out: ListConstraintsForPortfolioOutput = {}  # type: ignore[typeddict-item]
    if "ConstraintDetails" in data:
        import capo_service_catalog.types.constraint_details

        out["constraint_details"] = (
            capo_service_catalog.types.constraint_details.deserialize_aws_json_1_1(
                data["ConstraintDetails"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
