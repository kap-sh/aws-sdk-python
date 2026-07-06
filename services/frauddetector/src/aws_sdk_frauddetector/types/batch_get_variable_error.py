"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchGetVariableError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.integer2
    import aws_sdk_frauddetector.types.string


class BatchGetVariableError(TypedDict, closed=True):
    name: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The error name. </p>"""
    code: "aws_sdk_frauddetector.types.integer2.Integer2"
    """<p>The error code. </p>"""
    message: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetVariableError) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["code"] = value.get("code", 0)
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetVariableError:
    out: BatchGetVariableError = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    if "message" in data:
        out["message"] = data["message"]
    return out
