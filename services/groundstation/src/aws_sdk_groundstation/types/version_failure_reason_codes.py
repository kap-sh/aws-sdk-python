"""Generated from Smithy shape ``com.amazonaws.groundstation#VersionFailureReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.version_failure_reason_code

VersionFailureReasonCodes: TypeAlias = list[
    "aws_sdk_groundstation.types.version_failure_reason_code.VersionFailureReasonCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionFailureReasonCodes) -> list:
    import aws_sdk_groundstation.types.version_failure_reason_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.version_failure_reason_code.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VersionFailureReasonCodes:
    import aws_sdk_groundstation.types.version_failure_reason_code

    out: VersionFailureReasonCodes = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.version_failure_reason_code.deserialize_json(
                item
            )
        )
    return out
