"""Generated from Smithy shape ``com.amazonaws.ec2#ClientConnectResponseOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_endpoint_attribute_status
    import capo_ec2.types.string


class ClientConnectResponseOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether client connect options are enabled.</p>"""
    lambda_function_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.</p>"""
    status: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_attribute_status.ClientVpnEndpointAttributeStatus"
    ]
    """<p>The status of any updates to the client connect options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientConnectResponseOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "lambda_function_arn" in value:
        pairs.append(
            (f"{key_prefix}LambdaFunctionArn", str(value["lambda_function_arn"]))
        )
    if "status" in value:
        import capo_ec2.types.client_vpn_endpoint_attribute_status

        capo_ec2.types.client_vpn_endpoint_attribute_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> ClientConnectResponseOptions:
    out: ClientConnectResponseOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_lambda_function_arn = el.find("lambdaFunctionArn")
    if child_lambda_function_arn is not None:
        out["lambda_function_arn"] = str(child_lambda_function_arn.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_endpoint_attribute_status

        out["status"] = (
            capo_ec2.types.client_vpn_endpoint_attribute_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
