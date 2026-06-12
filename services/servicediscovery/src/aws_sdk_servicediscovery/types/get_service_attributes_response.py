"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetServiceAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.service_attributes


class GetServiceAttributesResponse(TypedDict):
    service_attributes: NotRequired[
        "aws_sdk_servicediscovery.types.service_attributes.ServiceAttributes"
    ]
    """<p>A complex type that contains the service ARN and a list of attribute key-value pairs associated with the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceAttributesResponse) -> dict:
    out: dict = {}
    if "service_attributes" in value:
        import aws_sdk_servicediscovery.types.service_attributes

        out["ServiceAttributes"] = (
            aws_sdk_servicediscovery.types.service_attributes.serialize_aws_json_1_1(
                value["service_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceAttributesResponse:
    out: GetServiceAttributesResponse = {}  # type: ignore[typeddict-item]
    if "ServiceAttributes" in data:
        import aws_sdk_servicediscovery.types.service_attributes

        out["service_attributes"] = (
            aws_sdk_servicediscovery.types.service_attributes.deserialize_aws_json_1_1(
                data["ServiceAttributes"]
            )
        )
    return out
