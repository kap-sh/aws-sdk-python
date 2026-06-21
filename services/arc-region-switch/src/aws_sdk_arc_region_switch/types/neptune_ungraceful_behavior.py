"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#NeptuneUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

NeptuneUngracefulBehavior: TypeAlias = Literal["failover",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NeptuneUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NeptuneUngracefulBehavior:
    return cast(NeptuneUngracefulBehavior, data)
