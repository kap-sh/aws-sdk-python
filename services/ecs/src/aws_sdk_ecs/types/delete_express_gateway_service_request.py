"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteExpressGatewayServiceRequest(TypedDict):
    service_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to delete. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExpressGatewayServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExpressGatewayServiceRequest:
    out: DeleteExpressGatewayServiceRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "DeleteExpressGatewayServiceRequest.service_arn required"
        )
    return out
