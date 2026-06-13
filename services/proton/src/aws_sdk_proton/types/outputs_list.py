"""Generated from Smithy shape ``com.amazonaws.proton#OutputsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.output

OutputsList: TypeAlias = list["aws_sdk_proton.types.output.Output"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputsList) -> list:
    import aws_sdk_proton.types.output

    out: list = []
    for item in value:
        out.append(aws_sdk_proton.types.output.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> OutputsList:
    import aws_sdk_proton.types.output

    out: OutputsList = []
    for item in data:
        out.append(aws_sdk_proton.types.output.deserialize_aws_json_1_0(item))
    return out
