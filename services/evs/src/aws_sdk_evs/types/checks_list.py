"""Generated from Smithy shape ``com.amazonaws.evs#ChecksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.check

ChecksList: TypeAlias = list["aws_sdk_evs.types.check.Check"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChecksList) -> list:
    import aws_sdk_evs.types.check

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.check.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ChecksList:
    import aws_sdk_evs.types.check

    out: ChecksList = []
    for item in data:
        out.append(aws_sdk_evs.types.check.deserialize_aws_json_1_0(item))
    return out
