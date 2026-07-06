"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAccountDataRetentionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.data_retention_mode
    import aws_sdk_bedrock.types.timestamp


class GetAccountDataRetentionResponse(TypedDict, closed=True):
    mode: "aws_sdk_bedrock.types.data_retention_mode.DataRetentionMode"
    """<p>The data retention mode configured for the account.</p>"""
    updated_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the data retention mode was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountDataRetentionResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.data_retention_mode

    out["mode"] = aws_sdk_bedrock.types.data_retention_mode.serialize_json(
        value["mode"]
    )
    if "updated_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAccountDataRetentionResponse:
    out: GetAccountDataRetentionResponse = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_bedrock.types.data_retention_mode

        out["mode"] = aws_sdk_bedrock.types.data_retention_mode.deserialize_json(
            data["mode"]
        )
    else:
        raise DeserializationError("GetAccountDataRetentionResponse.mode required")
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
