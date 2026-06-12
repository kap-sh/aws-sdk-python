"""Generated from Smithy shape ``com.amazonaws.controltower#RemediationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.remediation_type

RemediationTypes: TypeAlias = list[
    "aws_sdk_controltower.types.remediation_type.RemediationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationTypes) -> list:
    import aws_sdk_controltower.types.remediation_type

    out: list = []
    for item in value:
        out.append(aws_sdk_controltower.types.remediation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemediationTypes:
    import aws_sdk_controltower.types.remediation_type

    out: RemediationTypes = []
    for item in data:
        out.append(aws_sdk_controltower.types.remediation_type.deserialize_json(item))
    return out
