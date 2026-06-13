"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.lambdas

LambdaList: TypeAlias = list["aws_sdk_arc_region_switch.types.lambdas.Lambdas"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaList) -> list:
    import aws_sdk_arc_region_switch.types.lambdas

    out: list = []
    for item in value:
        out.append(aws_sdk_arc_region_switch.types.lambdas.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaList:
    import aws_sdk_arc_region_switch.types.lambdas

    out: LambdaList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.lambdas.deserialize_aws_json_1_0(item)
        )
    return out
