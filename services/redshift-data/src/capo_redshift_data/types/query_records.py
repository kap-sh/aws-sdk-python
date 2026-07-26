"""Generated from Smithy shape ``com.amazonaws.redshiftdata#QueryRecords``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift_data.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class _QueryRecords_CSVRecords(TypedDict, closed=True):
    CSVRecords: "capo_redshift_data.types.string.String"


QueryRecords: TypeAlias = _QueryRecords_CSVRecords


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRecords) -> dict:
    if "CSVRecords" in value:
        return {"CSVRecords": value["CSVRecords"]}
    else:
        raise SerializationError("QueryRecords: no variant present")


def deserialize_aws_json_1_1(data: dict) -> QueryRecords:
    if "CSVRecords" in data:
        return {"CSVRecords": data["CSVRecords"]}
    else:
        raise DeserializationError("QueryRecords: no recognized variant key")
