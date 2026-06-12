"""Generated from Smithy shape ``com.amazonaws.opensearch#NaturalLanguageQueryGenerationOptionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.natural_language_query_generation_current_state
    import aws_sdk_opensearch.types.natural_language_query_generation_desired_state


class NaturalLanguageQueryGenerationOptionsOutput(TypedDict):
    desired_state: NotRequired[
        "aws_sdk_opensearch.types.natural_language_query_generation_desired_state.NaturalLanguageQueryGenerationDesiredState"
    ]
    """<p>The desired state of the natural language query generation feature. Valid values are ENABLED and DISABLED.</p>"""
    current_state: NotRequired[
        "aws_sdk_opensearch.types.natural_language_query_generation_current_state.NaturalLanguageQueryGenerationCurrentState"
    ]
    """<p>The current state of the natural language query generation feature, indicating completion, in progress, or failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NaturalLanguageQueryGenerationOptionsOutput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import aws_sdk_opensearch.types.natural_language_query_generation_desired_state

        out["DesiredState"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "current_state" in value:
        import aws_sdk_opensearch.types.natural_language_query_generation_current_state

        out["CurrentState"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_current_state.serialize_json(
                value["current_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> NaturalLanguageQueryGenerationOptionsOutput:
    out: NaturalLanguageQueryGenerationOptionsOutput = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        import aws_sdk_opensearch.types.natural_language_query_generation_desired_state

        out["desired_state"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if "CurrentState" in data:
        import aws_sdk_opensearch.types.natural_language_query_generation_current_state

        out["current_state"] = (
            aws_sdk_opensearch.types.natural_language_query_generation_current_state.deserialize_json(
                data["CurrentState"]
            )
        )
    return out
