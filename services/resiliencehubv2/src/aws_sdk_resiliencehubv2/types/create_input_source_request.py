"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateInputSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.resource_configuration


class CreateInputSourceRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    resource_configuration: (
        "aws_sdk_resiliencehubv2.types.resource_configuration.ResourceConfiguration"
    )
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputSourceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    import aws_sdk_resiliencehubv2.types.resource_configuration

    out["resourceConfiguration"] = (
        aws_sdk_resiliencehubv2.types.resource_configuration.serialize_json(
            value["resource_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateInputSourceRequest:
    out: CreateInputSourceRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("CreateInputSourceRequest.service_arn required")
    if "resourceConfiguration" in data:
        import aws_sdk_resiliencehubv2.types.resource_configuration

        out["resource_configuration"] = (
            aws_sdk_resiliencehubv2.types.resource_configuration.deserialize_json(
                data["resourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInputSourceRequest.resource_configuration required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
