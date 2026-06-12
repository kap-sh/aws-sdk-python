"""Generated from Smithy shape ``com.amazonaws.glue#StatementOutputData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string


class StatementOutputData(TypedDict):
    text_plain: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The code execution output in text format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementOutputData) -> dict:
    out: dict = {}
    if "text_plain" in value:
        out["TextPlain"] = value["text_plain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StatementOutputData:
    out: StatementOutputData = {}  # type: ignore[typeddict-item]
    if "TextPlain" in data:
        out["text_plain"] = data["TextPlain"]
    return out
