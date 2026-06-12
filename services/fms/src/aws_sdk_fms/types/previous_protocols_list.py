"""Generated from Smithy shape ``com.amazonaws.fms#PreviousProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.previous_list_version
    import aws_sdk_fms.types.protocols_list

PreviousProtocolsList: TypeAlias = dict[
    "aws_sdk_fms.types.previous_list_version.PreviousListVersion",
    "aws_sdk_fms.types.protocols_list.ProtocolsList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PreviousProtocolsList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fms.types.protocols_list

        out[key] = aws_sdk_fms.types.protocols_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviousProtocolsList:
    out: PreviousProtocolsList = {}
    for key, value in data.items():
        import aws_sdk_fms.types.protocols_list

        out[key] = aws_sdk_fms.types.protocols_list.deserialize_aws_json_1_1(value)
    return out
