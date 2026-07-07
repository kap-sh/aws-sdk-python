"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_answer_data


class EvaluationAnswerInput(TypedDict, closed=True):
    value: NotRequired[
        "aws_sdk_connect.types.evaluation_answer_data.EvaluationAnswerData"
    ]
    """<p>The value for an answer in a contact evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAnswerInput) -> dict:
    out: dict = {}
    if "value" in value:
        import aws_sdk_connect.types.evaluation_answer_data

        out["Value"] = aws_sdk_connect.types.evaluation_answer_data.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationAnswerInput:
    out: EvaluationAnswerInput = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import aws_sdk_connect.types.evaluation_answer_data

        out["value"] = aws_sdk_connect.types.evaluation_answer_data.deserialize_json(
            data["Value"]
        )
    return out
