"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ExportLensInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_version


class ExportLensInput(TypedDict):
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    lens_version: NotRequired["aws_sdk_wellarchitected.types.lens_version.LensVersion"]
    """<p>The lens version to be exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportLensInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportLensInput:
    out: ExportLensInput = {}  # type: ignore[typeddict-item]
    return out
