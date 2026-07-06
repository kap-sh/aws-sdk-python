"""Generated from Smithy shape ``com.amazonaws.ec2#ClientConnectResponseOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_attribute_status
    import aws_sdk_ec2.types.string


class ClientConnectResponseOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether client connect options are enabled.</p>"""
    lambda_function_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_attribute_status.ClientVpnEndpointAttributeStatus"
    ]
    """<p>The status of any updates to the client connect options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientConnectResponseOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "lambda_function_arn" in value:
        pairs.append((f"{prefix}.LambdaFunctionArn", str(value["lambda_function_arn"])))
    if "status" in value:
        import aws_sdk_ec2.types.client_vpn_endpoint_attribute_status

        aws_sdk_ec2.types.client_vpn_endpoint_attribute_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> ClientConnectResponseOptions:
    out: ClientConnectResponseOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_lambda_function_arn = el.find("LambdaFunctionArn")
    if child_lambda_function_arn is not None:
        out["lambda_function_arn"] = str(child_lambda_function_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.client_vpn_endpoint_attribute_status

        out["status"] = (
            aws_sdk_ec2.types.client_vpn_endpoint_attribute_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
