"""Generated from Smithy shape ``com.amazonaws.transfer#State``."""

from typing import Literal, TypeAlias, cast

"""<p>Describes the condition of a file transfer protocol-enabled server with respect to its ability to perform file operations. There are six possible states: <code>OFFLINE</code>, <code>ONLINE</code>, <code>STARTING</code>, <code>STOPPING</code>, <code>START_FAILED</code>, and <code>STOP_FAILED</code>.</p> <p> <code>OFFLINE</code> indicates that the server exists, but that it is not available for file operations. <code>ONLINE</code> indicates that the server is available to perform file operations. <code>STARTING</code> indicates that the server's was instantiated, but the server is not yet available to perform file operations. Under normal conditions, it can take a couple of minutes for the server to be completely operational. Both <code>START_FAILED</code> and <code>STOP_FAILED</code> are error conditions.</p>"""
State: TypeAlias = Literal[
    "OFFLINE",
    "ONLINE",
    "STARTING",
    "STOPPING",
    "START_FAILED",
    "STOP_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: State) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> State:
    return cast(State, data)
