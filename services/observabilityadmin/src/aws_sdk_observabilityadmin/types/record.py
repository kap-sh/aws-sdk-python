"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.record_format


class Record(TypedDict, closed=True):
    data: NotRequired["str"]
    """<p>The data content of the test record used for pipeline validation.</p>"""
    type: NotRequired["aws_sdk_observabilityadmin.types.record_format.RecordFormat"]
    """<p>The type of the test record, indicating the format or category of the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> dict:
    out: dict = {}
    if "data" in value:
        out["Data"] = value["data"]
    if "type" in value:
        import aws_sdk_observabilityadmin.types.record_format

        out["Type"] = aws_sdk_observabilityadmin.types.record_format.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        out["data"] = data["Data"]
    if "Type" in data:
        import aws_sdk_observabilityadmin.types.record_format

        out["type"] = aws_sdk_observabilityadmin.types.record_format.deserialize_json(
            data["Type"]
        )
    return out
