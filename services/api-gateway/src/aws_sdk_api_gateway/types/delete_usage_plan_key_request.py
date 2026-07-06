"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteUsagePlanKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteUsagePlanKeyRequest(TypedDict, closed=True):
    usage_plan_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.</p>"""
    key_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The Id of the UsagePlanKey resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUsagePlanKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUsagePlanKeyRequest:
    out: DeleteUsagePlanKeyRequest = {}  # type: ignore[typeddict-item]
    return out
