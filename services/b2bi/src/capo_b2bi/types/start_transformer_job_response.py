"""Generated from Smithy shape ``com.amazonaws.b2bi#StartTransformerJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.transformer_job_id


class StartTransformerJobResponse(TypedDict, closed=True):
    transformer_job_id: "capo_b2bi.types.transformer_job_id.TransformerJobId"
    """<p>Returns the unique, system-generated identifier for a transformer run.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartTransformerJobResponse) -> dict:
    out: dict = {}
    out["transformerJobId"] = value["transformer_job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartTransformerJobResponse:
    out: StartTransformerJobResponse = {}  # type: ignore[typeddict-item]
    if "transformerJobId" in data:
        out["transformer_job_id"] = data["transformerJobId"]
    else:
        raise DeserializationError(
            "StartTransformerJobResponse.transformer_job_id required"
        )
    return out
