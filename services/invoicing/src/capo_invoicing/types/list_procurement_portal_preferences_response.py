"""Generated from Smithy shape ``com.amazonaws.invoicing#ListProcurementPortalPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.procurement_portal_preference_summaries


class ListProcurementPortalPreferencesResponse(TypedDict, closed=True):
    procurement_portal_preferences: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_summaries.ProcurementPortalPreferenceSummaries"
    ]
    """<p>The list of procurement portal preferences associated with the Amazon Web Services account.</p>"""
    next_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The token to use to retrieve the next set of results, or null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProcurementPortalPreferencesResponse) -> dict:
    out: dict = {}
    if "procurement_portal_preferences" in value:
        import capo_invoicing.types.procurement_portal_preference_summaries

        out["ProcurementPortalPreferences"] = (
            capo_invoicing.types.procurement_portal_preference_summaries.serialize_aws_json_1_0(
                value["procurement_portal_preferences"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProcurementPortalPreferencesResponse:
    out: ListProcurementPortalPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferences" in data:
        import capo_invoicing.types.procurement_portal_preference_summaries

        out["procurement_portal_preferences"] = (
            capo_invoicing.types.procurement_portal_preference_summaries.deserialize_aws_json_1_0(
                data["ProcurementPortalPreferences"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
