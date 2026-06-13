"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListMLModelTransformJobsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.string_list


class ListMLModelTransformJobsOutput(TypedDict):
    ids: NotRequired["aws_sdk_neptunedata.types.string_list.StringList"]
    """<p>A page from the list of model transform IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMLModelTransformJobsOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_neptunedata.types.string_list

        out["ids"] = aws_sdk_neptunedata.types.string_list.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> ListMLModelTransformJobsOutput:
    out: ListMLModelTransformJobsOutput = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_neptunedata.types.string_list

        out["ids"] = aws_sdk_neptunedata.types.string_list.deserialize_json(data["ids"])
    return out
