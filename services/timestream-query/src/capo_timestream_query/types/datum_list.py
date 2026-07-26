"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DatumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.datum

DatumList: TypeAlias = list["capo_timestream_query.types.datum.Datum"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatumList) -> list:
    import capo_timestream_query.types.datum

    out: list = []
    for item in value:
        out.append(capo_timestream_query.types.datum.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DatumList:
    import capo_timestream_query.types.datum

    out: DatumList = []
    for item in data:
        out.append(capo_timestream_query.types.datum.deserialize_aws_json_1_0(item))
    return out
