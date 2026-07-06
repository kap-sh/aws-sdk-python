"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListMLModelTrainingJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.string_list


class ListMLModelTrainingJobsOutput(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_neptunedata.types.string_list.StringList"]
    """<p>A page of the list of model training job IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMLModelTrainingJobsOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_neptunedata.types.string_list

        out["ids"] = aws_sdk_neptunedata.types.string_list.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> ListMLModelTrainingJobsOutput:
    out: ListMLModelTrainingJobsOutput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_neptunedata.types.string_list

        out["ids"] = aws_sdk_neptunedata.types.string_list.deserialize_json(data["ids"])
    return out
