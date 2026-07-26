"""Generated from Smithy shape ``com.amazonaws.athena#datumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.datum

datumList: TypeAlias = list["capo_athena.types.datum.Datum"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: datumList) -> list:
    import capo_athena.types.datum

    out: list = []
    for item in value:
        out.append(capo_athena.types.datum.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> datumList:
    import capo_athena.types.datum

    out: datumList = []
    for item in data:
        out.append(capo_athena.types.datum.deserialize_aws_json_1_1(item))
    return out
