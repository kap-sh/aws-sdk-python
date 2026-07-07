"""Generated from Smithy shape ``com.amazonaws.bedrock#PutAccountDataRetentionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.data_retention_mode


class PutAccountDataRetentionRequest(TypedDict, closed=True):
    mode: "aws_sdk_bedrock.types.data_retention_mode.DataRetentionMode"
    """<p>The data retention mode to set for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDataRetentionRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.data_retention_mode

    out["mode"] = aws_sdk_bedrock.types.data_retention_mode.serialize_json(
        value["mode"]
    )
    return out


def deserialize_json(data: dict) -> PutAccountDataRetentionRequest:
    out: PutAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_bedrock.types.data_retention_mode

        out["mode"] = aws_sdk_bedrock.types.data_retention_mode.deserialize_json(
            data["mode"]
        )
    else:
        raise DeserializationError("PutAccountDataRetentionRequest.mode required")
    return out
