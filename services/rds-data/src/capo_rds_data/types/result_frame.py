"""Generated from Smithy shape ``com.amazonaws.rdsdata#ResultFrame``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.records
    import capo_rds_data.types.result_set_metadata


class ResultFrame(TypedDict, closed=True):
    result_set_metadata: NotRequired[
        "capo_rds_data.types.result_set_metadata.ResultSetMetadata"
    ]
    """<p>The result-set metadata in the result set.</p>"""
    records: NotRequired["capo_rds_data.types.records.Records"]
    """<p>The records in the result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultFrame) -> dict:
    out: dict = {}
    if "result_set_metadata" in value:
        import capo_rds_data.types.result_set_metadata

        out["resultSetMetadata"] = (
            capo_rds_data.types.result_set_metadata.serialize_json(
                value["result_set_metadata"]
            )
        )
    if "records" in value:
        import capo_rds_data.types.records

        out["records"] = capo_rds_data.types.records.serialize_json(value["records"])
    return out


def deserialize_json(data: dict) -> ResultFrame:
    out: ResultFrame = {}  # type: ignore[typeddict-item]
    if "resultSetMetadata" in data:
        import capo_rds_data.types.result_set_metadata

        out["result_set_metadata"] = (
            capo_rds_data.types.result_set_metadata.deserialize_json(
                data["resultSetMetadata"]
            )
        )
    if "records" in data:
        import capo_rds_data.types.records

        out["records"] = capo_rds_data.types.records.deserialize_json(data["records"])
    return out
