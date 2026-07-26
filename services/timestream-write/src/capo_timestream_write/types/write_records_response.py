"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#WriteRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.records_ingested


class WriteRecordsResponse(TypedDict, closed=True):
    records_ingested: NotRequired[
        "capo_timestream_write.types.records_ingested.RecordsIngested"
    ]
    """<p>Information on the records ingested by this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WriteRecordsResponse) -> dict:
    out: dict = {}
    if "records_ingested" in value:
        import capo_timestream_write.types.records_ingested

        out["RecordsIngested"] = (
            capo_timestream_write.types.records_ingested.serialize_aws_json_1_0(
                value["records_ingested"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WriteRecordsResponse:
    out: WriteRecordsResponse = {}  # type: ignore[typeddict-item]
    if "RecordsIngested" in data:
        import capo_timestream_write.types.records_ingested

        out["records_ingested"] = (
            capo_timestream_write.types.records_ingested.deserialize_aws_json_1_0(
                data["RecordsIngested"]
            )
        )
    return out
