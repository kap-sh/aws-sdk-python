"""Generated from Smithy shape ``com.amazonaws.opensearch#AIMLOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.aiml_options_output
    import aws_sdk_opensearch.types.option_status


class AIMLOptionsStatus(TypedDict):
    options: NotRequired[
        "aws_sdk_opensearch.types.aiml_options_output.AIMLOptionsOutput"
    ]
    """<p>Machine learning options on the specified domain.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.option_status.OptionStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: AIMLOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_opensearch.types.aiml_options_output

        out["Options"] = aws_sdk_opensearch.types.aiml_options_output.serialize_json(
            value["options"]
        )
    if "status" in value:
        import aws_sdk_opensearch.types.option_status

        out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AIMLOptionsStatus:
    out: AIMLOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.aiml_options_output

        out["options"] = aws_sdk_opensearch.types.aiml_options_output.deserialize_json(
            data["Options"]
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
