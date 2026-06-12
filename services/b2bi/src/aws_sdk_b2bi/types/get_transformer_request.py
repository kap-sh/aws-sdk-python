"""Generated from Smithy shape ``com.amazonaws.b2bi#GetTransformerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.transformer_id


class GetTransformerRequest(TypedDict):
    transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId"
    """<p>Specifies the system-assigned unique identifier for the transformer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTransformerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTransformerRequest:
    out: GetTransformerRequest = {}  # type: ignore[typeddict-item]
    return out
