"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_version


class GetLensInput(TypedDict, closed=True):
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    lens_version: NotRequired["capo_wellarchitected.types.lens_version.LensVersion"]
    """<p>The lens version to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLensInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLensInput:
    out: GetLensInput = {}  # type: ignore[typeddict-item]
    return out
