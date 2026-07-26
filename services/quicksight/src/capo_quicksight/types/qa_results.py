"""Generated from Smithy shape ``com.amazonaws.quicksight#QAResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.qa_result

QAResults: TypeAlias = list["capo_quicksight.types.qa_result.QAResult"]


# --- restJson1 ser/de ---
def serialize_json(value: QAResults) -> list:
    import capo_quicksight.types.qa_result

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.qa_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> QAResults:
    import capo_quicksight.types.qa_result

    out: QAResults = []
    for item in data:
        out.append(capo_quicksight.types.qa_result.deserialize_json(item))
    return out
