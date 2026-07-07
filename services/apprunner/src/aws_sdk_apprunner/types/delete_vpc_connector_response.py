"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteVpcConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.vpc_connector


class DeleteVpcConnectorResponse(TypedDict, closed=True):
    vpc_connector: "aws_sdk_apprunner.types.vpc_connector.VpcConnector"
    """<p>A description of the App Runner VPC connector that this request just deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcConnectorResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.vpc_connector

    out["VpcConnector"] = aws_sdk_apprunner.types.vpc_connector.serialize_aws_json_1_0(
        value["vpc_connector"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcConnectorResponse:
    out: DeleteVpcConnectorResponse = {}  # type: ignore[typeddict-item]
    if "VpcConnector" in data:
        import aws_sdk_apprunner.types.vpc_connector

        out["vpc_connector"] = (
            aws_sdk_apprunner.types.vpc_connector.deserialize_aws_json_1_0(
                data["VpcConnector"]
            )
        )
    else:
        raise DeserializationError("DeleteVpcConnectorResponse.vpc_connector required")
    return out
