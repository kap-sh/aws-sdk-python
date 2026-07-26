"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StartCodegenJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_job


class StartCodegenJobResponse(TypedDict, closed=True):
    entity: NotRequired["capo_amplifyuibuilder.types.codegen_job.CodegenJob"]
    """<p>The code generation job for a UI component that is associated with an Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodegenJobResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import capo_amplifyuibuilder.types.codegen_job

        out["entity"] = capo_amplifyuibuilder.types.codegen_job.serialize_json(
            value["entity"]
        )
    return out


def deserialize_json(data: dict) -> StartCodegenJobResponse:
    out: StartCodegenJobResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import capo_amplifyuibuilder.types.codegen_job

        out["entity"] = capo_amplifyuibuilder.types.codegen_job.deserialize_json(
            data["entity"]
        )
    return out
