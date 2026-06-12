"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.arn
    import aws_sdk_servicediscovery.types.service_change


class UpdateServiceRequest(TypedDict):
    id: "aws_sdk_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that you want to update. If the namespace associated with the service is shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i> </p>"""
    service: "aws_sdk_servicediscovery.types.service_change.ServiceChange"
    """<p>A complex type that contains the new settings for the service. You can specify a maximum of 30 attributes (key-value pairs).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_servicediscovery.types.service_change

    out["Service"] = (
        aws_sdk_servicediscovery.types.service_change.serialize_aws_json_1_1(
            value["service"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceRequest:
    out: UpdateServiceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateServiceRequest.id required")
    if "Service" in data:
        import aws_sdk_servicediscovery.types.service_change

        out["service"] = (
            aws_sdk_servicediscovery.types.service_change.deserialize_aws_json_1_1(
                data["Service"]
            )
        )
    else:
        raise DeserializationError("UpdateServiceRequest.service required")
    return out
