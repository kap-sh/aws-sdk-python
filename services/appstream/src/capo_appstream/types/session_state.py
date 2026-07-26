"""Generated from Smithy shape ``com.amazonaws.appstream#SessionState``."""

from typing import Literal, TypeAlias, cast

"""<p>Possible values for the state of a streaming session.</p>"""
SessionState: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    return cast(SessionState, data)
