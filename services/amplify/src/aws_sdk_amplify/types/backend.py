"""Generated from Smithy shape ``com.amazonaws.amplify#Backend``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.stack_arn


class Backend(TypedDict, closed=True):
    stack_arn: NotRequired["aws_sdk_amplify.types.stack_arn.StackArn"]
    """<p>The Amazon Resource Name (ARN) for the CloudFormation stack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Backend) -> dict:
    out: dict = {}
    if "stack_arn" in value:
        out["stackArn"] = value["stack_arn"]
    return out


def deserialize_json(data: dict) -> Backend:
    out: Backend = {}  # type: ignore[typeddict-item]
    if "stackArn" in data:
        out["stack_arn"] = data["stackArn"]
    return out
