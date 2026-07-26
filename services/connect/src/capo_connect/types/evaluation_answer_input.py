"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_answer_data


class EvaluationAnswerInput(TypedDict, closed=True):
    value: NotRequired["capo_connect.types.evaluation_answer_data.EvaluationAnswerData"]
    """<p>The value for an answer in a contact evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAnswerInput) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_connect.types.evaluation_answer_data

        out["Value"] = capo_connect.types.evaluation_answer_data.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationAnswerInput:
    out: EvaluationAnswerInput = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import capo_connect.types.evaluation_answer_data

        out["value"] = capo_connect.types.evaluation_answer_data.deserialize_json(
            data["Value"]
        )
    return out
