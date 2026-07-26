"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeEndpointGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_group


class DescribeEndpointGroupResponse(TypedDict, closed=True):
    endpoint_group: NotRequired[
        "capo_global_accelerator.types.endpoint_group.EndpointGroup"
    ]
    """<p>The description of an endpoint group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointGroupResponse) -> dict:
    out: dict = {}
    if "endpoint_group" in value:
        import capo_global_accelerator.types.endpoint_group

        out["EndpointGroup"] = (
            capo_global_accelerator.types.endpoint_group.serialize_aws_json_1_1(
                value["endpoint_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointGroupResponse:
    out: DescribeEndpointGroupResponse = {}  # type: ignore[typeddict-item]
    if "EndpointGroup" in data:
        import capo_global_accelerator.types.endpoint_group

        out["endpoint_group"] = (
            capo_global_accelerator.types.endpoint_group.deserialize_aws_json_1_1(
                data["EndpointGroup"]
            )
        )
    return out
