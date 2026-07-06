"""Generated from Smithy shape ``com.amazonaws.controltower#ListBaselinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baselines


class ListBaselinesOutput(TypedDict, closed=True):
    baselines: "aws_sdk_controltower.types.baselines.Baselines"
    """<p>A list of <code>Baseline</code> object details.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBaselinesOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.baselines

    out["baselines"] = aws_sdk_controltower.types.baselines.serialize_json(
        value["baselines"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBaselinesOutput:
    out: ListBaselinesOutput = {}  # type: ignore[typeddict-item]
    if "baselines" in data:
        import aws_sdk_controltower.types.baselines

        out["baselines"] = aws_sdk_controltower.types.baselines.deserialize_json(
            data["baselines"]
        )
    else:
        raise DeserializationError("ListBaselinesOutput.baselines required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
