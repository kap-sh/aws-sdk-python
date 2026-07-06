"""Generated from Smithy shape ``com.amazonaws.mgn#StartCutoverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.job


class StartCutoverResponse(TypedDict, closed=True):
    job: NotRequired["aws_sdk_mgn.types.job.Job"]
    """<p>Start Cutover Job response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCutoverResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_mgn.types.job

        out["job"] = aws_sdk_mgn.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> StartCutoverResponse:
    out: StartCutoverResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_mgn.types.job

        out["job"] = aws_sdk_mgn.types.job.deserialize_json(data["job"])
    return out
