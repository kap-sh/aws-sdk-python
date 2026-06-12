"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateVpcConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.vpc_connector


class CreateVpcConnectorResponse(TypedDict):
    vpc_connector: "aws_sdk_apprunner.types.vpc_connector.VpcConnector"
    """<p>A description of the App Runner VPC connector that's created by this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcConnectorResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.vpc_connector

    out["VpcConnector"] = aws_sdk_apprunner.types.vpc_connector.serialize_aws_json_1_0(
        value["vpc_connector"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcConnectorResponse:
    out: CreateVpcConnectorResponse = {}  # type: ignore[typeddict-item]
    if "VpcConnector" in data:
        import aws_sdk_apprunner.types.vpc_connector

        out["vpc_connector"] = (
            aws_sdk_apprunner.types.vpc_connector.deserialize_aws_json_1_0(
                data["VpcConnector"]
            )
        )
    else:
        raise DeserializationError("CreateVpcConnectorResponse.vpc_connector required")
    return out
