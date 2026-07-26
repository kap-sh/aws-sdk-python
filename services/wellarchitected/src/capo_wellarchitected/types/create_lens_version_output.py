"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateLensVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_version


class CreateLensVersionOutput(TypedDict, closed=True):
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    lens_version: NotRequired["capo_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLensVersionOutput) -> dict:
    out: dict = {}
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "lens_version" in value:
        out["LensVersion"] = value["lens_version"]
    return out


def deserialize_json(data: dict) -> CreateLensVersionOutput:
    out: CreateLensVersionOutput = {}  # type: ignore[typeddict-item]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "LensVersion" in data:
        out["lens_version"] = data["LensVersion"]
    return out
