"""Generated from Smithy shape ``com.amazonaws.apigateway#UsagePlans``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_usage_plan
    import aws_sdk_api_gateway.types.string


class UsagePlans(TypedDict):
    items: NotRequired["aws_sdk_api_gateway.types.list_of_usage_plan.ListOfUsagePlan"]
    """<p>The current page of elements from this collection.</p>"""
    position: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsagePlans) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_api_gateway.types.list_of_usage_plan

        out["item"] = aws_sdk_api_gateway.types.list_of_usage_plan.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> UsagePlans:
    out: UsagePlans = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_usage_plan

        out["items"] = aws_sdk_api_gateway.types.list_of_usage_plan.deserialize_json(
            data["item"]
        )
    return out
