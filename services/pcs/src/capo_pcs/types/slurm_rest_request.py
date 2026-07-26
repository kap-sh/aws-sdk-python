"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmRestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.slurm_rest_mode


class SlurmRestRequest(TypedDict, closed=True):
    mode: "capo_pcs.types.slurm_rest_mode.SlurmRestMode"
    """<p>The default value for <code>mode</code> is <code>NONE</code>. A value of <code>STANDARD</code> means the Slurm REST API is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmRestRequest) -> dict:
    out: dict = {}
    import capo_pcs.types.slurm_rest_mode

    out["mode"] = capo_pcs.types.slurm_rest_mode.serialize_aws_json_1_0(value["mode"])
    return out


def deserialize_aws_json_1_0(data: dict) -> SlurmRestRequest:
    out: SlurmRestRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import capo_pcs.types.slurm_rest_mode

        out["mode"] = capo_pcs.types.slurm_rest_mode.deserialize_aws_json_1_0(
            data["mode"]
        )
    else:
        raise DeserializationError("SlurmRestRequest.mode required")
    return out
