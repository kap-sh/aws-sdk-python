"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateSlurmRestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pcs.types.slurm_rest_mode


class UpdateSlurmRestRequest(TypedDict):
    mode: NotRequired["aws_sdk_pcs.types.slurm_rest_mode.SlurmRestMode"]
    """<p>The default value for <code>mode</code> is <code>NONE</code>. A value of <code>STANDARD</code> means the Slurm REST API is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSlurmRestRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_pcs.types.slurm_rest_mode

        out["mode"] = aws_sdk_pcs.types.slurm_rest_mode.serialize_aws_json_1_0(
            value["mode"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSlurmRestRequest:
    out: UpdateSlurmRestRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_pcs.types.slurm_rest_mode

        out["mode"] = aws_sdk_pcs.types.slurm_rest_mode.deserialize_aws_json_1_0(
            data["mode"]
        )
    return out
