"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsCategoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.category_properties


class GetCallAnalyticsCategoryResponse(TypedDict, closed=True):
    category_properties: NotRequired[
        "capo_transcribe.types.category_properties.CategoryProperties"
    ]
    """<p>Provides you with the properties of the Call Analytics category you specified in your <code>GetCallAnalyticsCategory</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsCategoryResponse) -> dict:
    out: dict = {}
    if "category_properties" in value:
        import capo_transcribe.types.category_properties

        out["CategoryProperties"] = (
            capo_transcribe.types.category_properties.serialize_aws_json_1_1(
                value["category_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsCategoryResponse:
    out: GetCallAnalyticsCategoryResponse = {}  # type: ignore[typeddict-item]
    if "CategoryProperties" in data:
        import capo_transcribe.types.category_properties

        out["category_properties"] = (
            capo_transcribe.types.category_properties.deserialize_aws_json_1_1(
                data["CategoryProperties"]
            )
        )
    return out
