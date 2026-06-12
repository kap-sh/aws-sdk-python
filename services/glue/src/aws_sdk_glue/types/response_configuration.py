"""Generated from Smithy shape ``com.amazonaws.glue#ResponseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.json_path_string


class ResponseConfiguration(TypedDict):
    result_path: "aws_sdk_glue.types.json_path_string.JsonPathString"
    """<p>The JSON path expression that identifies where the actual result data is located within the API response.</p>"""
    error_path: NotRequired["aws_sdk_glue.types.json_path_string.JsonPathString"]
    """<p>The JSON path expression that identifies where error information is located within API responses when requests fail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseConfiguration) -> dict:
    out: dict = {}
    out["ResultPath"] = value["result_path"]
    if "error_path" in value:
        out["ErrorPath"] = value["error_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseConfiguration:
    out: ResponseConfiguration = {}  # type: ignore[typeddict-item]
    if "ResultPath" in data:
        out["result_path"] = data["ResultPath"]
    else:
        raise DeserializationError("ResponseConfiguration.result_path required")
    if "ErrorPath" in data:
        out["error_path"] = data["ErrorPath"]
    return out
