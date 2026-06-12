"""Generated from Smithy shape ``com.amazonaws.athena#datumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.datum

datumList: TypeAlias = list["aws_sdk_athena.types.datum.Datum"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: datumList) -> list:
    import aws_sdk_athena.types.datum

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.datum.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> datumList:
    import aws_sdk_athena.types.datum

    out: datumList = []
    for item in data:
        out.append(aws_sdk_athena.types.datum.deserialize_aws_json_1_1(item))
    return out
