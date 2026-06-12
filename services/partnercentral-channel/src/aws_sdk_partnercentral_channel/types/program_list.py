"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program

ProgramList: TypeAlias = list["aws_sdk_partnercentral_channel.types.program.Program"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramList) -> list:
    import aws_sdk_partnercentral_channel.types.program

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_channel.types.program.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProgramList:
    import aws_sdk_partnercentral_channel.types.program

    out: ProgramList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_channel.types.program.deserialize_aws_json_1_0(item)
        )
    return out
