"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_output


class ProtectedJobResult(TypedDict, closed=True):
    output: "capo_cleanrooms.types.protected_job_output.ProtectedJobOutput"
    """<p> The output of the protected job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobResult) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job_output

    out["output"] = capo_cleanrooms.types.protected_job_output.serialize_json(
        value["output"]
    )
    return out


def deserialize_json(data: dict) -> ProtectedJobResult:
    out: ProtectedJobResult = {}  # type: ignore[typeddict-item]
    if "output" in data:
        import capo_cleanrooms.types.protected_job_output

        out["output"] = capo_cleanrooms.types.protected_job_output.deserialize_json(
            data["output"]
        )
    else:
        raise DeserializationError("ProtectedJobResult.output required")
    return out
