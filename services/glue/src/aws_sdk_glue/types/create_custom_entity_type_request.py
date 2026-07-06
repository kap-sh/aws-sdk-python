"""Generated from Smithy shape ``com.amazonaws.glue#CreateCustomEntityTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.context_words
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.tags_map


class CreateCustomEntityTypeRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per Amazon Web Services account.</p>"""
    regex_string: "aws_sdk_glue.types.name_string.NameString"
    """<p>A regular expression string that is used for detecting sensitive data in a custom pattern.</p>"""
    context_words: NotRequired["aws_sdk_glue.types.context_words.ContextWords"]
    """<p>A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.</p> <p>If no context words are passed only a regular expression is checked.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>A list of tags applied to the custom entity type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomEntityTypeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RegexString"] = value["regex_string"]
    if "context_words" in value:
        import aws_sdk_glue.types.context_words

        out["ContextWords"] = aws_sdk_glue.types.context_words.serialize_aws_json_1_1(
            value["context_words"]
        )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomEntityTypeRequest:
    out: CreateCustomEntityTypeRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCustomEntityTypeRequest.name required")
    if "RegexString" in data:
        out["regex_string"] = data["RegexString"]
    else:
        raise DeserializationError(
            "CreateCustomEntityTypeRequest.regex_string required"
        )
    if "ContextWords" in data:
        import aws_sdk_glue.types.context_words

        out["context_words"] = (
            aws_sdk_glue.types.context_words.deserialize_aws_json_1_1(
                data["ContextWords"]
            )
        )
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
