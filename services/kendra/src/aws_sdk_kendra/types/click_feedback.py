"""Generated from Smithy shape ``com.amazonaws.kendra#ClickFeedback``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.result_id
    import aws_sdk_kendra.types.timestamp


class ClickFeedback(TypedDict, closed=True):
    result_id: "aws_sdk_kendra.types.result_id.ResultId"
    """<p>The identifier of the search result that was clicked.</p>"""
    click_time: "aws_sdk_kendra.types.timestamp.Timestamp"
    """<p>The Unix timestamp when the result was clicked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClickFeedback) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    import aws_sdk_kendra.types.timestamp

    out["ClickTime"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
        value["click_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClickFeedback:
    out: ClickFeedback = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    else:
        raise DeserializationError("ClickFeedback.result_id required")
    if "ClickTime" in data:
        import aws_sdk_kendra.types.timestamp

        out["click_time"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["ClickTime"]
        )
    else:
        raise DeserializationError("ClickFeedback.click_time required")
    return out
