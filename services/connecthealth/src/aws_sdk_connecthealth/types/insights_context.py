"""Generated from Smithy shape ``com.amazonaws.connecthealth#InsightsContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.insights_type


class InsightsContext(TypedDict, closed=True):
    insights_type: "aws_sdk_connecthealth.types.insights_type.InsightsType"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsContext) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.insights_type

    out["insightsType"] = aws_sdk_connecthealth.types.insights_type.serialize_json(
        value["insights_type"]
    )
    return out


def deserialize_json(data: dict) -> InsightsContext:
    out: InsightsContext = {}  # type: ignore[typeddict-item]
    if "insightsType" in data:
        import aws_sdk_connecthealth.types.insights_type

        out["insights_type"] = (
            aws_sdk_connecthealth.types.insights_type.deserialize_json(
                data["insightsType"]
            )
        )
    else:
        raise DeserializationError("InsightsContext.insights_type required")
    return out
