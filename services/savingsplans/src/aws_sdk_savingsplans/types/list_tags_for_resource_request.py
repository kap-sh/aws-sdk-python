"""Generated from Smithy shape ``com.amazonaws.savingsplans#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_savingsplans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_savingsplans.types.savings_plan_arn.SavingsPlanArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
