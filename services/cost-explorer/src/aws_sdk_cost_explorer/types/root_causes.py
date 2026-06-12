"""Generated from Smithy shape ``com.amazonaws.costexplorer#RootCauses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.root_cause

RootCauses: TypeAlias = list["aws_sdk_cost_explorer.types.root_cause.RootCause"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RootCauses) -> list:
    import aws_sdk_cost_explorer.types.root_cause

    out: list = []
    for item in value:
        out.append(aws_sdk_cost_explorer.types.root_cause.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RootCauses:
    import aws_sdk_cost_explorer.types.root_cause

    out: RootCauses = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.root_cause.deserialize_aws_json_1_1(item)
        )
    return out
