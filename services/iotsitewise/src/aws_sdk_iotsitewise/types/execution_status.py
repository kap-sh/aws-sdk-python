"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.execution_state


class ExecutionStatus(TypedDict, closed=True):
    state: "aws_sdk_iotsitewise.types.execution_state.ExecutionState"
    """<p>The current state of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.execution_state

    out["state"] = aws_sdk_iotsitewise.types.execution_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> ExecutionStatus:
    out: ExecutionStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.execution_state

        out["state"] = aws_sdk_iotsitewise.types.execution_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("ExecutionStatus.state required")
    return out
