"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeArchives``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.tape_archive

TapeArchives: TypeAlias = list["capo_storage_gateway.types.tape_archive.TapeArchive"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeArchives) -> list:
    import capo_storage_gateway.types.tape_archive

    out: list = []
    for item in value:
        out.append(capo_storage_gateway.types.tape_archive.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TapeArchives:
    import capo_storage_gateway.types.tape_archive

    out: TapeArchives = []
    for item in data:
        out.append(
            capo_storage_gateway.types.tape_archive.deserialize_aws_json_1_1(item)
        )
    return out
