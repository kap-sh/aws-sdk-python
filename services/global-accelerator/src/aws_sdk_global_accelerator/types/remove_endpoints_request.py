"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#RemoveEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_identifiers
    import aws_sdk_global_accelerator.types.generic_string


class RemoveEndpointsRequest(TypedDict, closed=True):
    endpoint_identifiers: (
        "aws_sdk_global_accelerator.types.endpoint_identifiers.EndpointIdentifiers"
    )
    """<p>The identifiers of the endpoints that you want to remove.</p>"""
    endpoint_group_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveEndpointsRequest) -> dict:
    out: dict = {}
    import aws_sdk_global_accelerator.types.endpoint_identifiers

    out["EndpointIdentifiers"] = (
        aws_sdk_global_accelerator.types.endpoint_identifiers.serialize_aws_json_1_1(
            value["endpoint_identifiers"]
        )
    )
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveEndpointsRequest:
    out: RemoveEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "EndpointIdentifiers" in data:
        import aws_sdk_global_accelerator.types.endpoint_identifiers

        out["endpoint_identifiers"] = (
            aws_sdk_global_accelerator.types.endpoint_identifiers.deserialize_aws_json_1_1(
                data["EndpointIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveEndpointsRequest.endpoint_identifiers required"
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        raise DeserializationError("RemoveEndpointsRequest.endpoint_group_arn required")
    return out
