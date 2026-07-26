"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DiagnosticsMode``."""

from typing import Literal, TypeAlias, cast

DiagnosticsMode: TypeAlias = Literal[
    "OFF",
    "SEND_ACTIVE_DTCS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DiagnosticsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DiagnosticsMode:
    return cast(DiagnosticsMode, data)
