"""Generated from Smithy shape ``com.amazonaws.directconnect#LagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.lag

LagList: TypeAlias = list["aws_sdk_direct_connect.types.lag.Lag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LagList) -> list:
    import aws_sdk_direct_connect.types.lag

    out: list = []
    for item in value:
        out.append(aws_sdk_direct_connect.types.lag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LagList:
    import aws_sdk_direct_connect.types.lag

    out: LagList = []
    for item in data:
        out.append(aws_sdk_direct_connect.types.lag.deserialize_aws_json_1_1(item))
    return out
