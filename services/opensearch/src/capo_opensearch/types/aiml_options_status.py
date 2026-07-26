"""Generated from Smithy shape ``com.amazonaws.opensearch#AIMLOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.aiml_options_output
    import capo_opensearch.types.option_status


class AIMLOptionsStatus(TypedDict, closed=True):
    options: NotRequired["capo_opensearch.types.aiml_options_output.AIMLOptionsOutput"]
    """<p>Machine learning options on the specified domain.</p>"""
    status: NotRequired["capo_opensearch.types.option_status.OptionStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: AIMLOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_opensearch.types.aiml_options_output

        out["Options"] = capo_opensearch.types.aiml_options_output.serialize_json(
            value["options"]
        )
    if "status" in value:
        import capo_opensearch.types.option_status

        out["Status"] = capo_opensearch.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AIMLOptionsStatus:
    out: AIMLOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.aiml_options_output

        out["options"] = capo_opensearch.types.aiml_options_output.deserialize_json(
            data["Options"]
        )
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
