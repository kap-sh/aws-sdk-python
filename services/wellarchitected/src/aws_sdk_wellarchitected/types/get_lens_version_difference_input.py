"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensVersionDifferenceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_version


class GetLensVersionDifferenceInput(TypedDict, closed=True):
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    base_lens_version: NotRequired[
        "aws_sdk_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The base version of the lens.</p>"""
    target_lens_version: NotRequired[
        "aws_sdk_wellarchitected.types.lens_version.LensVersion"
    ]
    """<p>The lens version to target a difference for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLensVersionDifferenceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLensVersionDifferenceInput:
    out: GetLensVersionDifferenceInput = {}  # type: ignore[typeddict-item]
    return out
