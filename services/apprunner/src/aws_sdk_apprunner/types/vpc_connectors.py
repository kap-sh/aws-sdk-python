"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcConnectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.vpc_connector

VpcConnectors: TypeAlias = list["aws_sdk_apprunner.types.vpc_connector.VpcConnector"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcConnectors) -> list:
    import aws_sdk_apprunner.types.vpc_connector

    out: list = []
    for item in value:
        out.append(aws_sdk_apprunner.types.vpc_connector.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VpcConnectors:
    import aws_sdk_apprunner.types.vpc_connector

    out: VpcConnectors = []
    for item in data:
        out.append(aws_sdk_apprunner.types.vpc_connector.deserialize_aws_json_1_0(item))
    return out
