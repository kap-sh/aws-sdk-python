"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.venice_global_arn


class GetPolicyInput(TypedDict):
    arn: "aws_sdk_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which the policy need to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyInput:
    out: GetPolicyInput = {}  # type: ignore[typeddict-item]
    return out
