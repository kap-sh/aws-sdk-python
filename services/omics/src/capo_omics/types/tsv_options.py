"""Generated from Smithy shape ``com.amazonaws.omics#TsvOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_options


class TsvOptions(TypedDict, closed=True):
    read_options: NotRequired["capo_omics.types.read_options.ReadOptions"]
    """<p>The file's read options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TsvOptions) -> dict:
    out: dict = {}
    if "read_options" in value:
        import capo_omics.types.read_options

        out["readOptions"] = capo_omics.types.read_options.serialize_json(
            value["read_options"]
        )
    return out


def deserialize_json(data: dict) -> TsvOptions:
    out: TsvOptions = {}  # type: ignore[typeddict-item]
    if "readOptions" in data:
        import capo_omics.types.read_options

        out["read_options"] = capo_omics.types.read_options.deserialize_json(
            data["readOptions"]
        )
    return out
