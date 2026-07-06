"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetImportFileTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string


class GetImportFileTaskRequest(TypedDict, closed=True):
    id: "aws_sdk_migrationhubstrategy.types.string.String"
    """<p> The ID of the import file task. This ID is returned in the response of <a>StartImportFileTask</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportFileTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportFileTaskRequest:
    out: GetImportFileTaskRequest = {}  # type: ignore[typeddict-item]
    return out
