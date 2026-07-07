"""Generated from Smithy shape ``com.amazonaws.transcribe#CategoryProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.category_name
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.input_type
    import aws_sdk_transcribe.types.rule_list
    import aws_sdk_transcribe.types.tag_list


class CategoryProperties(TypedDict, closed=True):
    category_name: NotRequired["aws_sdk_transcribe.types.category_name.CategoryName"]
    """<p>The name of the Call Analytics category. Category names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    rules: NotRequired["aws_sdk_transcribe.types.rule_list.RuleList"]
    """<p>The rules used to define a Call Analytics category. Each category can have between 1 and 20 rules.</p>"""
    create_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics category was created.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    last_update_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics category was last updated.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-05T12:45:32.691000-07:00</code> represents 12:45 PM UTC-7 on May 5, 2022.</p>"""
    tags: NotRequired["aws_sdk_transcribe.types.tag_list.TagList"]
    """<p>The tags, each in the form of a key:value pair, assigned to the specified call analytics category.</p>"""
    input_type: NotRequired["aws_sdk_transcribe.types.input_type.InputType"]
    """<p>The input type associated with the specified category. <code>POST_CALL</code> refers to a category that is applied to batch transcriptions; <code>REAL_TIME</code> refers to a category that is applied to streaming transcriptions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoryProperties) -> dict:
    out: dict = {}
    if "category_name" in value:
        out["CategoryName"] = value["category_name"]
    if "rules" in value:
        import aws_sdk_transcribe.types.rule_list

        out["Rules"] = aws_sdk_transcribe.types.rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    if "create_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["CreateTime"] = aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["LastUpdateTime"] = (
            aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_update_time"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> CategoryProperties:
    out: CategoryProperties = {}  # type: ignore[typeddict-item]
    if "CategoryName" in data:
        out["category_name"] = data["CategoryName"]
    if "Rules" in data:
        import aws_sdk_transcribe.types.rule_list

        out["rules"] = aws_sdk_transcribe.types.rule_list.deserialize_aws_json_1_1(
            data["Rules"]
        )
    if "CreateTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["create_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    if "LastUpdateTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["last_update_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
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
