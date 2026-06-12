"""Generated from Smithy shape ``com.amazonaws.eventbridge#TestEventPatternResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.boolean


class TestEventPatternResponse(TypedDict):
    result: "aws_sdk_eventbridge.types.boolean.Boolean"
    """<p>Indicates whether the event matches the event pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestEventPatternResponse) -> dict:
    out: dict = {}
    out["Result"] = value.get("result", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> TestEventPatternResponse:
    out: TestEventPatternResponse = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        out["result"] = data["Result"]
    else:
        out["result"] = False
    return out
