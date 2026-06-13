"""Generated from Smithy shape ``com.amazonaws.backup#DeleteFrameworkInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.framework_name


class DeleteFrameworkInput(TypedDict):
    framework_name: "aws_sdk_backup.types.framework_name.FrameworkName"
    """<p>The unique name of a framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFrameworkInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFrameworkInput:
    out: DeleteFrameworkInput = {}  # type: ignore[typeddict-item]
    return out
