"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateCallAnalyticsCategoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.category_name
    import aws_sdk_transcribe.types.input_type
    import aws_sdk_transcribe.types.rule_list
    import aws_sdk_transcribe.types.tag_list


class CreateCallAnalyticsCategoryRequest(TypedDict):
    category_name: "aws_sdk_transcribe.types.category_name.CategoryName"
    """<p>A unique name, chosen by you, for your Call Analytics category. It's helpful to use a detailed naming system that will make sense to you in the future. For example, it's better to use <code>sentiment-positive-last30seconds</code> for a category over a generic name like <code>test-category</code>.</p> <p>Category names are case sensitive.</p>"""
    rules: "aws_sdk_transcribe.types.rule_list.RuleList"
    """<p>Rules define a Call Analytics category. When creating a new category, you must create between 1 and 20 rules for that category. For each rule, you specify a filter you want applied to the attributes of a call. For example, you can choose a sentiment filter that detects if a customer's sentiment was positive during the last 30 seconds of the call.</p>"""
    tags: NotRequired["aws_sdk_transcribe.types.tag_list.TagList"]
    r"""<p>Adds one or more custom tags, each in the form of a key:value pair, to a new call analytics category at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html\">Tagging resources</a>.</p>"""
    input_type: NotRequired["aws_sdk_transcribe.types.input_type.InputType"]
    """<p>Choose whether you want to create a real-time or a post-call category for your Call Analytics transcription.</p> <p>Specifying <code>POST_CALL</code> assigns your category to post-call transcriptions; categories with this input type cannot be applied to streaming (real-time) transcriptions.</p> <p>Specifying <code>REAL_TIME</code> assigns your category to streaming transcriptions; categories with this input type cannot be applied to post-call transcriptions.</p> <p>If you do not include <code>InputType</code>, your category is created as a post-call category by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCallAnalyticsCategoryRequest) -> dict:
    out: dict = {}
    import aws_sdk_transcribe.types.rule_list

    out["Rules"] = aws_sdk_transcribe.types.rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    if "tags" in value:
        import aws_sdk_transcribe.types.tag_list

        out["Tags"] = aws_sdk_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "input_type" in value:
        import aws_sdk_transcribe.types.input_type

        out["InputType"] = aws_sdk_transcribe.types.input_type.serialize_aws_json_1_1(
            value["input_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCallAnalyticsCategoryRequest:
    out: CreateCallAnalyticsCategoryRequest = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_transcribe.types.rule_list

        out["rules"] = aws_sdk_transcribe.types.rule_list.deserialize_aws_json_1_1(
            data["Rules"]
        )
    else:
        raise DeserializationError("CreateCallAnalyticsCategoryRequest.rules required")
    if "Tags" in data:
        import aws_sdk_transcribe.types.tag_list

        out["tags"] = aws_sdk_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "InputType" in data:
        import aws_sdk_transcribe.types.input_type

        out["input_type"] = (
            aws_sdk_transcribe.types.input_type.deserialize_aws_json_1_1(
                data["InputType"]
            )
        )
    return out
