"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartProtectedJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job


class StartProtectedJobOutput(TypedDict):
    protected_job: "aws_sdk_cleanrooms.types.protected_job.ProtectedJob"
    """<p> The protected job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProtectedJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job

    out["protectedJob"] = aws_sdk_cleanrooms.types.protected_job.serialize_json(
        value["protected_job"]
    )
    return out


def deserialize_json(data: dict) -> StartProtectedJobOutput:
    out: StartProtectedJobOutput = {}  # type: ignore[typeddict-item]
    if "protectedJob" in data:
        import aws_sdk_cleanrooms.types.protected_job

        out["protected_job"] = aws_sdk_cleanrooms.types.protected_job.deserialize_json(
            data["protectedJob"]
        )
    else:
        raise DeserializationError("StartProtectedJobOutput.protected_job required")
    return out
