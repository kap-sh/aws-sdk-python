"""Generated from Smithy shape ``com.amazonaws.backup#DeleteFrameworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.framework_name


class DeleteFrameworkInput(TypedDict, closed=True):
    framework_name: "capo_backup.types.framework_name.FrameworkName"
    """<p>The unique name of a framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFrameworkInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFrameworkInput:
    out: DeleteFrameworkInput = {}  # type: ignore[typeddict-item]
    return out
