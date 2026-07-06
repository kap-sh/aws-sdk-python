"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AddEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_descriptions
    import aws_sdk_global_accelerator.types.generic_string


class AddEndpointsResponse(TypedDict, closed=True):
    endpoint_descriptions: NotRequired[
        "aws_sdk_global_accelerator.types.endpoint_descriptions.EndpointDescriptions"
    ]
    """<p>The list of endpoint objects.</p>"""
    endpoint_group_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoint_descriptions" in value:
        import aws_sdk_global_accelerator.types.endpoint_descriptions

        out["EndpointDescriptions"] = (
            aws_sdk_global_accelerator.types.endpoint_descriptions.serialize_aws_json_1_1(
                value["endpoint_descriptions"]
            )
        )
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddEndpointsResponse:
    out: AddEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointDescriptions" in data:
        import aws_sdk_global_accelerator.types.endpoint_descriptions

        out["endpoint_descriptions"] = (
            aws_sdk_global_accelerator.types.endpoint_descriptions.deserialize_aws_json_1_1(
                data["EndpointDescriptions"]
            )
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    return out
