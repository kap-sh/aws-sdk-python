"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ImportApplicationUsageResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.import_id


class ImportApplicationUsageResult(TypedDict):
    import_id: "aws_sdk_applicationcostprofiler.types.import_id.ImportId"
    """<p>ID of the import request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportApplicationUsageResult) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    return out


def deserialize_json(data: dict) -> ImportApplicationUsageResult:
    out: ImportApplicationUsageResult = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    else:
        raise DeserializationError("ImportApplicationUsageResult.import_id required")
    return out
