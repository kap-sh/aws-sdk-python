"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetAction``."""

from typing import Literal, TypeAlias, cast

FleetAction: TypeAlias = Literal["AUTO_SCALING",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetAction:
    return cast(FleetAction, data)
