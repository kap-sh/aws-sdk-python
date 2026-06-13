"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.target_id
    import aws_sdk_networkflowmonitor.types.target_type


class TargetIdentifier(TypedDict):
    target_id: "aws_sdk_networkflowmonitor.types.target_id.TargetId"
    """<p>The identifier for a target, which is currently always an account ID .</p>"""
    target_type: "aws_sdk_networkflowmonitor.types.target_type.TargetType"
    """<p>The type of a target. A target type is currently always <code>ACCOUNT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetIdentifier) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.target_id

    out["targetId"] = aws_sdk_networkflowmonitor.types.target_id.serialize_json(
        value["target_id"]
    )
    import aws_sdk_networkflowmonitor.types.target_type

    out["targetType"] = aws_sdk_networkflowmonitor.types.target_type.serialize_json(
        value["target_type"]
    )
    return out


def deserialize_json(data: dict) -> TargetIdentifier:
    out: TargetIdentifier = {}  # type: ignore[typeddict-item]
    if "targetId" in data:
        import aws_sdk_networkflowmonitor.types.target_id

        out["target_id"] = aws_sdk_networkflowmonitor.types.target_id.deserialize_json(
            data["targetId"]
        )
    else:
        raise DeserializationError("TargetIdentifier.target_id required")
    if "targetType" in data:
        import aws_sdk_networkflowmonitor.types.target_type

        out["target_type"] = (
            aws_sdk_networkflowmonitor.types.target_type.deserialize_json(
                data["targetType"]
            )
        )
    else:
        raise DeserializationError("TargetIdentifier.target_type required")
    return out
