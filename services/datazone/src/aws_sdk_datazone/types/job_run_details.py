"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_run_details


class _JobRunDetails_lineageRunDetails(TypedDict):
    lineageRunDetails: "aws_sdk_datazone.types.lineage_run_details.LineageRunDetails"


JobRunDetails: TypeAlias = _JobRunDetails_lineageRunDetails


# --- restJson1 ser/de ---
def serialize_json(value: JobRunDetails) -> dict:
    if "lineageRunDetails" in value:
        import aws_sdk_datazone.types.lineage_run_details

        return {
            "lineageRunDetails": aws_sdk_datazone.types.lineage_run_details.serialize_json(
                value["lineageRunDetails"]
            )
        }
    else:
        raise SerializationError("JobRunDetails: no variant present")


def deserialize_json(data: dict) -> JobRunDetails:
    if "lineageRunDetails" in data:
        import aws_sdk_datazone.types.lineage_run_details

        return {
            "lineageRunDetails": aws_sdk_datazone.types.lineage_run_details.deserialize_json(
                data["lineageRunDetails"]
            )
        }
    else:
        raise DeserializationError("JobRunDetails: no recognized variant key")
