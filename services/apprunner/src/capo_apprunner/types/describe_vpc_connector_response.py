"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeVpcConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.vpc_connector


class DescribeVpcConnectorResponse(TypedDict, closed=True):
    vpc_connector: "capo_apprunner.types.vpc_connector.VpcConnector"
    """<p>A description of the App Runner VPC connector that you specified in this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVpcConnectorResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.vpc_connector

    out["VpcConnector"] = capo_apprunner.types.vpc_connector.serialize_aws_json_1_0(
        value["vpc_connector"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVpcConnectorResponse:
    out: DescribeVpcConnectorResponse = {}  # type: ignore[typeddict-item]
    if "VpcConnector" in data:
        import capo_apprunner.types.vpc_connector

        out["vpc_connector"] = (
            capo_apprunner.types.vpc_connector.deserialize_aws_json_1_0(
                data["VpcConnector"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVpcConnectorResponse.vpc_connector required"
        )
    return out
