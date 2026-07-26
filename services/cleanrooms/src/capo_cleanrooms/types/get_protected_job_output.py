"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetProtectedJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job


class GetProtectedJobOutput(TypedDict, closed=True):
    protected_job: "capo_cleanrooms.types.protected_job.ProtectedJob"
    """<p> The protected job metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProtectedJobOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job

    out["protectedJob"] = capo_cleanrooms.types.protected_job.serialize_json(
        value["protected_job"]
    )
    return out


def deserialize_json(data: dict) -> GetProtectedJobOutput:
    out: GetProtectedJobOutput = {}  # type: ignore[typeddict-item]
    if "protectedJob" in data:
        import capo_cleanrooms.types.protected_job

        out["protected_job"] = capo_cleanrooms.types.protected_job.deserialize_json(
            data["protectedJob"]
        )
    else:
        raise DeserializationError("GetProtectedJobOutput.protected_job required")
    return out
