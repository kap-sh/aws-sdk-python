"""Generated from Smithy shape ``com.amazonaws.b2bi#DeleteTransformerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.transformer_id


class DeleteTransformerRequest(TypedDict, closed=True):
    transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId"
    """<p>Specifies the system-assigned unique identifier for the transformer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTransformerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTransformerRequest:
    out: DeleteTransformerRequest = {}  # type: ignore[typeddict-item]
    return out
