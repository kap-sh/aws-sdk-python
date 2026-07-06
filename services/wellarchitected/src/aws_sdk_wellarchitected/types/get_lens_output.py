"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens


class GetLensOutput(TypedDict, closed=True):
    lens: NotRequired["aws_sdk_wellarchitected.types.lens.Lens"]
    """<p>A lens return object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLensOutput) -> dict:
    out: dict = {}
    if "lens" in value:
        import aws_sdk_wellarchitected.types.lens

        out["Lens"] = aws_sdk_wellarchitected.types.lens.serialize_json(value["lens"])
    return out


def deserialize_json(data: dict) -> GetLensOutput:
    out: GetLensOutput = {}  # type: ignore[typeddict-item]
    if "Lens" in data:
        import aws_sdk_wellarchitected.types.lens

        out["lens"] = aws_sdk_wellarchitected.types.lens.deserialize_json(data["Lens"])
    return out
