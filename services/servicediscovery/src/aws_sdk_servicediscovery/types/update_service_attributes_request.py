"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateServiceAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.arn
    import aws_sdk_servicediscovery.types.service_attributes_map


class UpdateServiceAttributesRequest(TypedDict):
    service_id: "aws_sdk_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that you want to update. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN.</p>"""
    attributes: (
        "aws_sdk_servicediscovery.types.service_attributes_map.ServiceAttributesMap"
    )
    """<p>A string map that contains attribute key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceAttributesRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    import aws_sdk_servicediscovery.types.service_attributes_map

    out["Attributes"] = (
        aws_sdk_servicediscovery.types.service_attributes_map.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceAttributesRequest:
    out: UpdateServiceAttributesRequest = {}  # type: ignore[typeddict-item]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError("UpdateServiceAttributesRequest.service_id required")
    if "Attributes" in data:
        import aws_sdk_servicediscovery.types.service_attributes_map

        out["attributes"] = (
            aws_sdk_servicediscovery.types.service_attributes_map.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("UpdateServiceAttributesRequest.attributes required")
    return out
