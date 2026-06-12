"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DisruptionPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.disruption_type
    import aws_sdk_resiliencehub.types.failure_policy

DisruptionPolicy: TypeAlias = dict[
    "aws_sdk_resiliencehub.types.disruption_type.DisruptionType",
    "aws_sdk_resiliencehub.types.failure_policy.FailurePolicy",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DisruptionPolicy) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_resiliencehub.types.disruption_type
        import aws_sdk_resiliencehub.types.failure_policy

        out[aws_sdk_resiliencehub.types.disruption_type.serialize_json(key)] = (
            aws_sdk_resiliencehub.types.failure_policy.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> DisruptionPolicy:
    out: DisruptionPolicy = {}
    for key, value in data.items():
        import aws_sdk_resiliencehub.types.disruption_type
        import aws_sdk_resiliencehub.types.failure_policy

        out[aws_sdk_resiliencehub.types.disruption_type.deserialize_json(key)] = (
            aws_sdk_resiliencehub.types.failure_policy.deserialize_json(value)
        )
    return out
