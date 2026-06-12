"""Generated from Smithy shape ``com.amazonaws.guardduty#CountByCoverageStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_status
    import aws_sdk_guardduty.types.long

CountByCoverageStatus: TypeAlias = dict[
    "aws_sdk_guardduty.types.coverage_status.CoverageStatus",
    "aws_sdk_guardduty.types.long.Long",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CountByCoverageStatus) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_guardduty.types.coverage_status

        out[aws_sdk_guardduty.types.coverage_status.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> CountByCoverageStatus:
    out: CountByCoverageStatus = {}
    for key, value in data.items():
        import aws_sdk_guardduty.types.coverage_status

        out[aws_sdk_guardduty.types.coverage_status.deserialize_json(key)] = value
    return out
