"""Generated from Smithy shape ``com.amazonaws.iot#AlertTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.alert_target
    import aws_sdk_iot.types.alert_target_type

AlertTargets: TypeAlias = dict[
    "aws_sdk_iot.types.alert_target_type.AlertTargetType",
    "aws_sdk_iot.types.alert_target.AlertTarget",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AlertTargets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.alert_target
        import aws_sdk_iot.types.alert_target_type

        out[aws_sdk_iot.types.alert_target_type.serialize_json(key)] = (
            aws_sdk_iot.types.alert_target.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AlertTargets:
    out: AlertTargets = {}
    for key, value in data.items():
        import aws_sdk_iot.types.alert_target
        import aws_sdk_iot.types.alert_target_type

        out[aws_sdk_iot.types.alert_target_type.deserialize_json(key)] = (
            aws_sdk_iot.types.alert_target.deserialize_json(value)
        )
    return out
