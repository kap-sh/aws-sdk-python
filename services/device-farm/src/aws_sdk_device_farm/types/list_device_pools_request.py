"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListDevicePoolsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.device_pool_type
    import aws_sdk_device_farm.types.pagination_token


class ListDevicePoolsRequest(TypedDict, closed=True):
    arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The project ARN.</p>"""
    type: NotRequired["aws_sdk_device_farm.types.device_pool_type.DevicePoolType"]
    """<p>The device pools' type.</p> <p>Allowed values include:</p> <ul> <li> <p>CURATED: A device pool that is created and managed by AWS Device Farm.</p> </li> <li> <p>PRIVATE: A device pool that is created and managed by the device pool developer.</p> </li> </ul>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicePoolsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_device_farm.types.device_pool_type

        out["type"] = aws_sdk_device_farm.types.device_pool_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicePoolsRequest:
    out: ListDevicePoolsRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListDevicePoolsRequest.arn required")
    if "type" in data:
        import aws_sdk_device_farm.types.device_pool_type

        out["type"] = (
            aws_sdk_device_farm.types.device_pool_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
