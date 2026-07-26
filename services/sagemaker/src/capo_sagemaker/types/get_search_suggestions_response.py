"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetSearchSuggestionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.property_name_suggestion_list


class GetSearchSuggestionsResponse(TypedDict, closed=True):
    property_name_suggestions: NotRequired[
        "capo_sagemaker.types.property_name_suggestion_list.PropertyNameSuggestionList"
    ]
    """<p>A list of property names for a <code>Resource</code> that match a <code>SuggestionQuery</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSearchSuggestionsResponse) -> dict:
    out: dict = {}
    if "property_name_suggestions" in value:
        import capo_sagemaker.types.property_name_suggestion_list

        out["PropertyNameSuggestions"] = (
            capo_sagemaker.types.property_name_suggestion_list.serialize_aws_json_1_1(
                value["property_name_suggestions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSearchSuggestionsResponse:
    out: GetSearchSuggestionsResponse = {}  # type: ignore[typeddict-item]
    if "PropertyNameSuggestions" in data:
        import capo_sagemaker.types.property_name_suggestion_list

        out["property_name_suggestions"] = (
            capo_sagemaker.types.property_name_suggestion_list.deserialize_aws_json_1_1(
                data["PropertyNameSuggestions"]
            )
        )
    return out
