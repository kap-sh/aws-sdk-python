"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StartCodegenJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.start_codegen_job_data


class StartCodegenJobRequest(TypedDict, closed=True):
    app_id: "capo_amplifyuibuilder.types.app_id.AppId"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    client_token: NotRequired["str"]
    """<p>The idempotency token used to ensure that the code generation job request completes only once.</p>"""
    codegen_job_to_create: (
        "capo_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData"
    )
    """<p>The code generation job resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodegenJobRequest) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.start_codegen_job_data

    out["codegenJobToCreate"] = (
        capo_amplifyuibuilder.types.start_codegen_job_data.serialize_json(
            value["codegen_job_to_create"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartCodegenJobRequest:
    out: StartCodegenJobRequest = {}  # type: ignore[typeddict-item]
    if "codegenJobToCreate" in data:
        import capo_amplifyuibuilder.types.start_codegen_job_data

        out["codegen_job_to_create"] = (
            capo_amplifyuibuilder.types.start_codegen_job_data.deserialize_json(
                data["codegenJobToCreate"]
            )
        )
    else:
        raise DeserializationError(
            "StartCodegenJobRequest.codegen_job_to_create required"
        )
    return out
