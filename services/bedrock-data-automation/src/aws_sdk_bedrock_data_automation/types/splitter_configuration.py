"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SplitterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.state


class SplitterConfiguration(TypedDict, closed=True):
    state: NotRequired["aws_sdk_bedrock_data_automation.types.state.State"]


# --- restJson1 ser/de ---
def serialize_json(value: SplitterConfiguration) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_bedrock_data_automation.types.state

        out["state"] = aws_sdk_bedrock_data_automation.types.state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> SplitterConfiguration:
    out: SplitterConfiguration = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_bedrock_data_automation.types.state

        out["state"] = aws_sdk_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    return out
