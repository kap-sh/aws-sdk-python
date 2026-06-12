"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfS3DataAccesses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.s3_data_access_details

ListOfS3DataAccesses: TypeAlias = list[
    "aws_sdk_dataexchange.types.s3_data_access_details.S3DataAccessDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfS3DataAccesses) -> list:
    import aws_sdk_dataexchange.types.s3_data_access_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dataexchange.types.s3_data_access_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfS3DataAccesses:
    import aws_sdk_dataexchange.types.s3_data_access_details

    out: ListOfS3DataAccesses = []
    for item in data:
        out.append(
            aws_sdk_dataexchange.types.s3_data_access_details.deserialize_json(item)
        )
    return out
