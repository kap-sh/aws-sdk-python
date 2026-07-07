"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateCallAnalyticsCategoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.category_properties


class UpdateCallAnalyticsCategoryResponse(TypedDict, closed=True):
    category_properties: NotRequired[
        "aws_sdk_transcribe.types.category_properties.CategoryProperties"
    ]
    """<p>Provides you with the properties of the Call Analytics category you specified in your <code>UpdateCallAnalyticsCategory</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCallAnalyticsCategoryResponse) -> dict:
    out: dict = {}
    if "category_properties" in value:
        import aws_sdk_transcribe.types.category_properties

        out["CategoryProperties"] = (
            aws_sdk_transcribe.types.category_properties.serialize_aws_json_1_1(
                value["category_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCallAnalyticsCategoryResponse:
    out: UpdateCallAnalyticsCategoryResponse = {}  # type: ignore[typeddict-item]
    if "CategoryProperties" in data:
        import aws_sdk_transcribe.types.category_properties

        out["category_properties"] = (
            aws_sdk_transcribe.types.category_properties.deserialize_aws_json_1_1(
                data["CategoryProperties"]
            )
        )
    return out
