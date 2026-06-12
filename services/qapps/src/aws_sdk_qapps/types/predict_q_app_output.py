"""Generated from Smithy shape ``com.amazonaws.qapps#PredictQAppOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.predict_app_definition


class PredictQAppOutput(TypedDict):
    app: "aws_sdk_qapps.types.predict_app_definition.PredictAppDefinition"
    """<p>The generated Q App definition.</p>"""
    problem_statement: "str"
    """<p>The problem statement extracted from the input conversation, if provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAppOutput) -> dict:
    out: dict = {}
    import aws_sdk_qapps.types.predict_app_definition

    out["app"] = aws_sdk_qapps.types.predict_app_definition.serialize_json(value["app"])
    out["problemStatement"] = value["problem_statement"]
    return out


def deserialize_json(data: dict) -> PredictQAppOutput:
    out: PredictQAppOutput = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_qapps.types.predict_app_definition

        out["app"] = aws_sdk_qapps.types.predict_app_definition.deserialize_json(
            data["app"]
        )
    else:
        raise DeserializationError("PredictQAppOutput.app required")
    if "problemStatement" in data:
        out["problem_statement"] = data["problemStatement"]
    else:
        raise DeserializationError("PredictQAppOutput.problem_statement required")
    return out
