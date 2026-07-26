"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetCodegenJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_job


class GetCodegenJobResponse(TypedDict, closed=True):
    job: NotRequired["capo_amplifyuibuilder.types.codegen_job.CodegenJob"]
    """<p>The configuration settings for the code generation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodegenJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_amplifyuibuilder.types.codegen_job

        out["job"] = capo_amplifyuibuilder.types.codegen_job.serialize_json(
            value["job"]
        )
    return out


def deserialize_json(data: dict) -> GetCodegenJobResponse:
    out: GetCodegenJobResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import capo_amplifyuibuilder.types.codegen_job

        out["job"] = capo_amplifyuibuilder.types.codegen_job.deserialize_json(
            data["job"]
        )
    return out
