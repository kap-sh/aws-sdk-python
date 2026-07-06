"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CreateServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.service


class CreateServiceResponse(TypedDict, closed=True):
    service: NotRequired["aws_sdk_servicediscovery.types.service.Service"]
    """<p>A complex type that contains information about the new service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_servicediscovery.types.service

        out["Service"] = aws_sdk_servicediscovery.types.service.serialize_aws_json_1_1(
            value["service"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServiceResponse:
    out: CreateServiceResponse = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import aws_sdk_servicediscovery.types.service

        out["service"] = (
            aws_sdk_servicediscovery.types.service.deserialize_aws_json_1_1(
                data["Service"]
            )
        )
    return out
