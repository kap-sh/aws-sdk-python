"""Generated from Smithy shape ``com.amazonaws.glue#CustomEntityType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.context_words
    import capo_glue.types.name_string


class CustomEntityType(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per Amazon Web Services account.</p>"""
    regex_string: "capo_glue.types.name_string.NameString"
    """<p>A regular expression string that is used for detecting sensitive data in a custom pattern.</p>"""
    context_words: NotRequired["capo_glue.types.context_words.ContextWords"]
    """<p>A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.</p> <p>If no context words are passed only a regular expression is checked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomEntityType) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RegexString"] = value["regex_string"]
    if "context_words" in value:
        import capo_glue.types.context_words

        out["ContextWords"] = capo_glue.types.context_words.serialize_aws_json_1_1(
            value["context_words"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomEntityType:
    out: CustomEntityType = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomEntityType.name required")
    if "RegexString" in data:
        out["regex_string"] = data["RegexString"]
    else:
        raise DeserializationError("CustomEntityType.regex_string required")
    if "ContextWords" in data:
        import capo_glue.types.context_words

        out["context_words"] = capo_glue.types.context_words.deserialize_aws_json_1_1(
            data["ContextWords"]
        )
    return out
