"""Generated from Smithy shape ``com.amazonaws.neptunedata#SparqlRecordsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.sparql_record

SparqlRecordsList: TypeAlias = list[
    "aws_sdk_neptunedata.types.sparql_record.SparqlRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: SparqlRecordsList) -> list:
    import aws_sdk_neptunedata.types.sparql_record

    out: list = []
    for item in value:
        out.append(aws_sdk_neptunedata.types.sparql_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> SparqlRecordsList:
    import aws_sdk_neptunedata.types.sparql_record

    out: SparqlRecordsList = []
    for item in data:
        out.append(aws_sdk_neptunedata.types.sparql_record.deserialize_json(item))
    return out
