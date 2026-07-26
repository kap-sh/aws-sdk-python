"""Generated from Smithy shape ``com.amazonaws.workmail#ResourceDelegates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.delegate

ResourceDelegates: TypeAlias = list["capo_workmail.types.delegate.Delegate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDelegates) -> list:
    import capo_workmail.types.delegate

    out: list = []
    for item in value:
        out.append(capo_workmail.types.delegate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceDelegates:
    import capo_workmail.types.delegate

    out: ResourceDelegates = []
    for item in data:
        out.append(capo_workmail.types.delegate.deserialize_aws_json_1_1(item))
    return out
