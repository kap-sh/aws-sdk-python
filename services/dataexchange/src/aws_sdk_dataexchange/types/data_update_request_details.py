"""Generated from Smithy shape ``com.amazonaws.dataexchange#DataUpdateRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.timestamp


class DataUpdateRequestDetails(TypedDict, closed=True):
    data_updated_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>A datetime in the past when the data was updated. This typically means that the underlying resource supporting the data set was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataUpdateRequestDetails) -> dict:
    out: dict = {}
    if "data_updated_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["DataUpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["data_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DataUpdateRequestDetails:
    out: DataUpdateRequestDetails = {}  # type: ignore[typeddict-item]
    if "DataUpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["data_updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["DataUpdatedAt"]
        )
    return out
