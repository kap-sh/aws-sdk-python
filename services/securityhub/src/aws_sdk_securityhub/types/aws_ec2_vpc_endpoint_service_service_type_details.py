"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcEndpointServiceServiceTypeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2VpcEndpointServiceServiceTypeDetails(TypedDict):
    service_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcEndpointServiceServiceTypeDetails) -> dict:
    out: dict = {}
    if "service_type" in value:
        out["ServiceType"] = value["service_type"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpcEndpointServiceServiceTypeDetails:
    out: AwsEc2VpcEndpointServiceServiceTypeDetails = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        out["service_type"] = data["ServiceType"]
    return out
