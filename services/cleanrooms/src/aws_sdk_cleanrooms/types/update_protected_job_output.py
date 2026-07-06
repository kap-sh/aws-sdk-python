"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateProtectedJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job


class UpdateProtectedJobOutput(TypedDict, closed=True):
    protected_job: "aws_sdk_cleanrooms.types.protected_job.ProtectedJob"
    """<p>The protected job output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedJobOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job

    out["protectedJob"] = aws_sdk_cleanrooms.types.protected_job.serialize_json(
        value["protected_job"]
    )
    return out


def deserialize_json(data: dict) -> UpdateProtectedJobOutput:
    out: UpdateProtectedJobOutput = {}  # type: ignore[typeddict-item]
    if "protectedJob" in data:
        import aws_sdk_cleanrooms.types.protected_job

        out["protected_job"] = aws_sdk_cleanrooms.types.protected_job.deserialize_json(
            data["protectedJob"]
        )
    else:
        raise DeserializationError("UpdateProtectedJobOutput.protected_job required")
    return out
