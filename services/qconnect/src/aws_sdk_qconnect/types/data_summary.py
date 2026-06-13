"""Generated from Smithy shape ``com.amazonaws.qconnect#DataSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.data_details
    import aws_sdk_qconnect.types.data_reference


class DataSummary(TypedDict):
    reference: "aws_sdk_qconnect.types.data_reference.DataReference"
    """<p>Reference information about the content.</p>"""
    details: "aws_sdk_qconnect.types.data_details.DataDetails"
    """<p>Details about the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSummary) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.data_reference

    out["reference"] = aws_sdk_qconnect.types.data_reference.serialize_json(
        value["reference"]
    )
    import aws_sdk_qconnect.types.data_details

    out["details"] = aws_sdk_qconnect.types.data_details.serialize_json(
        value["details"]
    )
    return out


def deserialize_json(data: dict) -> DataSummary:
    out: DataSummary = {}  # type: ignore[typeddict-item]
    if "reference" in data:
        import aws_sdk_qconnect.types.data_reference

        out["reference"] = aws_sdk_qconnect.types.data_reference.deserialize_json(
            data["reference"]
        )
    else:
        raise DeserializationError("DataSummary.reference required")
    if "details" in data:
        import aws_sdk_qconnect.types.data_details

        out["details"] = aws_sdk_qconnect.types.data_details.deserialize_json(
            data["details"]
        )
    else:
        raise DeserializationError("DataSummary.details required")
    return out
