"""Generated from Smithy shape ``com.amazonaws.glue#NullCheckBoxList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_boolean


class NullCheckBoxList(TypedDict):
    is_empty: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies that an empty string is considered as a null value.</p>"""
    is_null_string: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies that a value spelling out the word 'null' is considered as a null value.</p>"""
    is_neg_one: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies that an integer value of -1 is considered as a null value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NullCheckBoxList) -> dict:
    out: dict = {}
    if "is_empty" in value:
        out["IsEmpty"] = value["is_empty"]
    if "is_null_string" in value:
        out["IsNullString"] = value["is_null_string"]
    if "is_neg_one" in value:
        out["IsNegOne"] = value["is_neg_one"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NullCheckBoxList:
    out: NullCheckBoxList = {}  # type: ignore[typeddict-item]
    if "IsEmpty" in data:
        out["is_empty"] = data["IsEmpty"]
    if "IsNullString" in data:
        out["is_null_string"] = data["IsNullString"]
    if "IsNegOne" in data:
        out["is_neg_one"] = data["IsNegOne"]
    return out
