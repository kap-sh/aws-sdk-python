"""Generated from Smithy shape ``com.amazonaws.translate#ListTextTranslationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_translate.types.next_token
    import aws_sdk_translate.types.text_translation_job_properties_list


class ListTextTranslationJobsResponse(TypedDict, closed=True):
    text_translation_job_properties_list: NotRequired[
        "aws_sdk_translate.types.text_translation_job_properties_list.TextTranslationJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["aws_sdk_translate.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTextTranslationJobsResponse) -> dict:
    out: dict = {}
    if "text_translation_job_properties_list" in value:
        import aws_sdk_translate.types.text_translation_job_properties_list

        out["TextTranslationJobPropertiesList"] = (
            aws_sdk_translate.types.text_translation_job_properties_list.serialize_aws_json_1_1(
                value["text_translation_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTextTranslationJobsResponse:
    out: ListTextTranslationJobsResponse = {}  # type: ignore[typeddict-item]
    if "TextTranslationJobPropertiesList" in data:
        import aws_sdk_translate.types.text_translation_job_properties_list

        out["text_translation_job_properties_list"] = (
            aws_sdk_translate.types.text_translation_job_properties_list.deserialize_aws_json_1_1(
                data["TextTranslationJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
