"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetResponsePlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class GetResponsePlanInput(TypedDict, closed=True):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResponsePlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResponsePlanInput:
    out: GetResponsePlanInput = {}  # type: ignore[typeddict-item]
    return out
