"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.tape_info

TapeInfos: TypeAlias = list["capo_storage_gateway.types.tape_info.TapeInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeInfos) -> list:
    import capo_storage_gateway.types.tape_info

    out: list = []
    for item in value:
        out.append(capo_storage_gateway.types.tape_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TapeInfos:
    import capo_storage_gateway.types.tape_info

    out: TapeInfos = []
    for item in data:
        out.append(capo_storage_gateway.types.tape_info.deserialize_aws_json_1_1(item))
    return out
