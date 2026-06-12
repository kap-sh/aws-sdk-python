"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsCategoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.category_properties


class GetCallAnalyticsCategoryResponse(TypedDict):
    category_properties: NotRequired[
        "aws_sdk_transcribe.types.category_properties.CategoryProperties"
    ]
    """<p>Provides you with the properties of the Call Analytics category you specified in your <code>GetCallAnalyticsCategory</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsCategoryResponse) -> dict:
    out: dict = {}
    if "category_properties" in value:
        import aws_sdk_transcribe.types.category_properties

        out["CategoryProperties"] = (
            aws_sdk_transcribe.types.category_properties.serialize_aws_json_1_1(
                value["category_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsCategoryResponse:
    out: GetCallAnalyticsCategoryResponse = {}  # type: ignore[typeddict-item]
    if "CategoryProperties" in data:
        import aws_sdk_transcribe.types.category_properties

        out["category_properties"] = (
            aws_sdk_transcribe.types.category_properties.deserialize_aws_json_1_1(
                data["CategoryProperties"]
            )
        )
    return out
