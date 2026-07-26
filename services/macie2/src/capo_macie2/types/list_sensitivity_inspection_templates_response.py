"""Generated from Smithy shape ``com.amazonaws.macie2#ListSensitivityInspectionTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_sensitivity_inspection_templates_entry
    import capo_macie2.types.__string


class ListSensitivityInspectionTemplatesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""
    sensitivity_inspection_templates: NotRequired[
        "capo_macie2.types.__list_of_sensitivity_inspection_templates_entry.__listOfSensitivityInspectionTemplatesEntry"
    ]
    """<p>An array that specifies the unique identifier and name of the sensitivity inspection template for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSensitivityInspectionTemplatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sensitivity_inspection_templates" in value:
        import capo_macie2.types.__list_of_sensitivity_inspection_templates_entry

        out["sensitivityInspectionTemplates"] = (
            capo_macie2.types.__list_of_sensitivity_inspection_templates_entry.serialize_json(
                value["sensitivity_inspection_templates"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSensitivityInspectionTemplatesResponse:
    out: ListSensitivityInspectionTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sensitivityInspectionTemplates" in data:
        import capo_macie2.types.__list_of_sensitivity_inspection_templates_entry

        out["sensitivity_inspection_templates"] = (
            capo_macie2.types.__list_of_sensitivity_inspection_templates_entry.deserialize_json(
                data["sensitivityInspectionTemplates"]
            )
        )
    return out
