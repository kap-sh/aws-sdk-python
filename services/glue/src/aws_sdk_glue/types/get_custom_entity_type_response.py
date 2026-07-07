"""Generated from Smithy shape ``com.amazonaws.glue#GetCustomEntityTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.context_words
    import aws_sdk_glue.types.name_string


class GetCustomEntityTypeResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the custom pattern that you retrieved.</p>"""
    regex_string: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>A regular expression string that is used for detecting sensitive data in a custom pattern.</p>"""
    context_words: NotRequired["aws_sdk_glue.types.context_words.ContextWords"]
    """<p>A list of context words if specified when you created the custom pattern. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCustomEntityTypeResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "regex_string" in value:
        out["RegexString"] = value["regex_string"]
    if "context_words" in value:
        import aws_sdk_glue.types.context_words

        out["ContextWords"] = aws_sdk_glue.types.context_words.serialize_aws_json_1_1(
            value["context_words"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCustomEntityTypeResponse:
    out: GetCustomEntityTypeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RegexString" in data:
        out["regex_string"] = data["RegexString"]
    if "ContextWords" in data:
        import aws_sdk_glue.types.context_words

        out["context_words"] = (
            aws_sdk_glue.types.context_words.deserialize_aws_json_1_1(
                data["ContextWords"]
            )
        )
    return out
