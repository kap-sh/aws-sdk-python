"""Generated from Smithy shape ``com.amazonaws.sagemaker#SuggestionQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.property_name_query


class SuggestionQuery(TypedDict, closed=True):
    property_name_query: NotRequired[
        "capo_sagemaker.types.property_name_query.PropertyNameQuery"
    ]
    """<p>Defines a property name hint. Only property names that begin with the specified hint are included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionQuery) -> dict:
    out: dict = {}
    if "property_name_query" in value:
        import capo_sagemaker.types.property_name_query

        out["PropertyNameQuery"] = (
            capo_sagemaker.types.property_name_query.serialize_aws_json_1_1(
                value["property_name_query"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuggestionQuery:
    out: SuggestionQuery = {}  # type: ignore[typeddict-item]
    if "PropertyNameQuery" in data:
        import capo_sagemaker.types.property_name_query

        out["property_name_query"] = (
            capo_sagemaker.types.property_name_query.deserialize_aws_json_1_1(
                data["PropertyNameQuery"]
            )
        )
    return out
