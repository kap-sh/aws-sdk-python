"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneOptionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.auto_tune_state
    import aws_sdk_elasticsearch_service.types.string


class AutoTuneOptionsOutput(TypedDict):
    state: NotRequired[
        "aws_sdk_elasticsearch_service.types.auto_tune_state.AutoTuneState"
    ]
    """<p>Specifies the <code>AutoTuneState</code> for the Elasticsearch domain.</p>"""
    error_message: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>Specifies the error message while enabling or disabling the Auto-Tune.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsOutput) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_elasticsearch_service.types.auto_tune_state

        out["State"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_state.serialize_json(
                value["state"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsOutput:
    out: AutoTuneOptionsOutput = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_elasticsearch_service.types.auto_tune_state

        out["state"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_state.deserialize_json(
                data["State"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
