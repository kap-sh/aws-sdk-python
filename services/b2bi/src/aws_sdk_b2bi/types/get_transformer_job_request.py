"""Generated from Smithy shape ``com.amazonaws.b2bi#GetTransformerJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.transformer_id
    import aws_sdk_b2bi.types.transformer_job_id


class GetTransformerJobRequest(TypedDict, closed=True):
    transformer_job_id: "aws_sdk_b2bi.types.transformer_job_id.TransformerJobId"
    """<p>Specifies the unique, system-generated identifier for a transformer run.</p>"""
    transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId"
    """<p>Specifies the system-assigned unique identifier for the transformer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTransformerJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTransformerJobRequest:
    out: GetTransformerJobRequest = {}  # type: ignore[typeddict-item]
    return out
