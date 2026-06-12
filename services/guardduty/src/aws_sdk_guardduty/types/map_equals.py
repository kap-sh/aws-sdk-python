"""Generated from Smithy shape ``com.amazonaws.guardduty#MapEquals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan_condition_pair

MapEquals: TypeAlias = list[
    "aws_sdk_guardduty.types.scan_condition_pair.ScanConditionPair"
]


# --- restJson1 ser/de ---
def serialize_json(value: MapEquals) -> list:
    import aws_sdk_guardduty.types.scan_condition_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.scan_condition_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> MapEquals:
    import aws_sdk_guardduty.types.scan_condition_pair

    out: MapEquals = []
    for item in data:
        out.append(aws_sdk_guardduty.types.scan_condition_pair.deserialize_json(item))
    return out
