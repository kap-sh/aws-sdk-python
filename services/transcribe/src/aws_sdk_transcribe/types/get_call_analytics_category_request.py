"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsCategoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.category_name


class GetCallAnalyticsCategoryRequest(TypedDict):
    category_name: "aws_sdk_transcribe.types.category_name.CategoryName"
    """<p>The name of the Call Analytics category you want information about. Category names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsCategoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsCategoryRequest:
    out: GetCallAnalyticsCategoryRequest = {}  # type: ignore[typeddict-item]
    return out
