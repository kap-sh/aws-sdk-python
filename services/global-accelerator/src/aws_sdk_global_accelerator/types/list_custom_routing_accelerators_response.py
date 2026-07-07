"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingAcceleratorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_accelerators
    import aws_sdk_global_accelerator.types.generic_string


class ListCustomRoutingAcceleratorsResponse(TypedDict, closed=True):
    accelerators: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_accelerators.CustomRoutingAccelerators"
    ]
    """<p>The list of custom routing accelerators for a customer account.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomRoutingAcceleratorsResponse) -> dict:
    out: dict = {}
    if "accelerators" in value:
        import aws_sdk_global_accelerator.types.custom_routing_accelerators

        out["Accelerators"] = (
            aws_sdk_global_accelerator.types.custom_routing_accelerators.serialize_aws_json_1_1(
                value["accelerators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomRoutingAcceleratorsResponse:
    out: ListCustomRoutingAcceleratorsResponse = {}  # type: ignore[typeddict-item]
    if "Accelerators" in data:
        import aws_sdk_global_accelerator.types.custom_routing_accelerators

        out["accelerators"] = (
            aws_sdk_global_accelerator.types.custom_routing_accelerators.deserialize_aws_json_1_1(
                data["Accelerators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
