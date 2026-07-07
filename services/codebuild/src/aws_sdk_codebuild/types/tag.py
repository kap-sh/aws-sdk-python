"""Generated from Smithy shape ``com.amazonaws.codebuild#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.key_input
    import aws_sdk_codebuild.types.value_input


class Tag(TypedDict, closed=True):
    key: NotRequired["aws_sdk_codebuild.types.key_input.KeyInput"]
    """<p>The tag's key.</p>"""
    value: NotRequired["aws_sdk_codebuild.types.value_input.ValueInput"]
    """<p>The tag's value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
