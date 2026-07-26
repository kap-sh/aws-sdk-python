"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoringStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_scoring_mode
    import capo_connect.types.evaluation_form_scoring_status


class EvaluationFormScoringStrategy(TypedDict, closed=True):
    mode: "capo_connect.types.evaluation_form_scoring_mode.EvaluationFormScoringMode"
    """<p>The scoring mode of the evaluation form.</p>"""
    status: (
        "capo_connect.types.evaluation_form_scoring_status.EvaluationFormScoringStatus"
    )
    """<p>The scoring status of the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormScoringStrategy) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_scoring_mode

    out["Mode"] = capo_connect.types.evaluation_form_scoring_mode.serialize_json(
        value["mode"]
    )
    import capo_connect.types.evaluation_form_scoring_status

    out["Status"] = capo_connect.types.evaluation_form_scoring_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormScoringStrategy:
    out: EvaluationFormScoringStrategy = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import capo_connect.types.evaluation_form_scoring_mode

        out["mode"] = capo_connect.types.evaluation_form_scoring_mode.deserialize_json(
            data["Mode"]
        )
    else:
        raise DeserializationError("EvaluationFormScoringStrategy.mode required")
    if "Status" in data:
        import capo_connect.types.evaluation_form_scoring_status

        out["status"] = (
            capo_connect.types.evaluation_form_scoring_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationFormScoringStrategy.status required")
    return out
