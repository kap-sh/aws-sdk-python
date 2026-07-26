"""Generated from Smithy shape ``com.amazonaws.athena#ApplicationDPUSizes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.name_string
    import capo_athena.types.supported_dpu_size_list


class ApplicationDPUSizes(TypedDict, closed=True):
    application_runtime_id: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>The name of the supported application runtime (for example, <code>Athena notebook version 1</code>).</p>"""
    supported_dpu_sizes: NotRequired[
        "capo_athena.types.supported_dpu_size_list.SupportedDPUSizeList"
    ]
    """<p>A list of the supported DPU sizes that the application runtime supports.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationDPUSizes) -> dict:
    out: dict = {}
    if "application_runtime_id" in value:
        out["ApplicationRuntimeId"] = value["application_runtime_id"]
    if "supported_dpu_sizes" in value:
        import capo_athena.types.supported_dpu_size_list

        out["SupportedDPUSizes"] = (
            capo_athena.types.supported_dpu_size_list.serialize_aws_json_1_1(
                value["supported_dpu_sizes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationDPUSizes:
    out: ApplicationDPUSizes = {}  # type: ignore[typeddict-item]
    if "ApplicationRuntimeId" in data:
        out["application_runtime_id"] = data["ApplicationRuntimeId"]
    if "SupportedDPUSizes" in data:
        import capo_athena.types.supported_dpu_size_list

        out["supported_dpu_sizes"] = (
            capo_athena.types.supported_dpu_size_list.deserialize_aws_json_1_1(
                data["SupportedDPUSizes"]
            )
        )
    return out
