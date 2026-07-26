"""Generated from Smithy shape ``com.amazonaws.rekognition#ConnectedHomeLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.connected_home_label

ConnectedHomeLabels: TypeAlias = list[
    "capo_rekognition.types.connected_home_label.ConnectedHomeLabel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedHomeLabels) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConnectedHomeLabels:
    return list(data)
