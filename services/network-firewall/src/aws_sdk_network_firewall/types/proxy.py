"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Proxy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.create_time
    import aws_sdk_network_firewall.types.delete_time
    import aws_sdk_network_firewall.types.failure_code
    import aws_sdk_network_firewall.types.failure_message
    import aws_sdk_network_firewall.types.listener_properties
    import aws_sdk_network_firewall.types.nat_gateway_id
    import aws_sdk_network_firewall.types.proxy_modify_state
    import aws_sdk_network_firewall.types.proxy_state
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tag_list
    import aws_sdk_network_firewall.types.tls_intercept_properties
    import aws_sdk_network_firewall.types.update_time


class Proxy(TypedDict, closed=True):
    create_time: NotRequired["aws_sdk_network_firewall.types.create_time.CreateTime"]
    """<p>Time the Proxy was created. </p>"""
    delete_time: NotRequired["aws_sdk_network_firewall.types.delete_time.DeleteTime"]
    """<p>Time the Proxy was deleted. </p>"""
    update_time: NotRequired["aws_sdk_network_firewall.types.update_time.UpdateTime"]
    """<p>Time the Proxy was updated. </p>"""
    failure_code: NotRequired["aws_sdk_network_firewall.types.failure_code.FailureCode"]
    """<p>Failure code for cases when the Proxy fails to attach or update. </p>"""
    failure_message: NotRequired[
        "aws_sdk_network_firewall.types.failure_message.FailureMessage"
    ]
    """<p>Failure message for cases when the Proxy fails to attach or update. </p>"""
    proxy_state: NotRequired["aws_sdk_network_firewall.types.proxy_state.ProxyState"]
    """<p>Current attachment/detachment status of the Proxy. </p>"""
    proxy_modify_state: NotRequired[
        "aws_sdk_network_firewall.types.proxy_modify_state.ProxyModifyState"
    ]
    """<p>Current modification status of the Proxy. </p>"""
    nat_gateway_id: NotRequired[
        "aws_sdk_network_firewall.types.nat_gateway_id.NatGatewayId"
    ]
    """<p>The NAT Gateway for the proxy. </p>"""
    proxy_configuration_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>"""
    proxy_configuration_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p>"""
    proxy_name: NotRequired["aws_sdk_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p>"""
    proxy_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p>"""
    listener_properties: NotRequired[
        "aws_sdk_network_firewall.types.listener_properties.ListenerProperties"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic. </p>"""
    tls_intercept_properties: NotRequired[
        "aws_sdk_network_firewall.types.tls_intercept_properties.TlsInterceptProperties"
    ]
    """<p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Proxy) -> dict:
    out: dict = {}
    if "create_time" in value:
        import aws_sdk_network_firewall.types.create_time

        out["CreateTime"] = (
            aws_sdk_network_firewall.types.create_time.serialize_aws_json_1_0(
                value["create_time"]
            )
        )
    if "delete_time" in value:
        import aws_sdk_network_firewall.types.delete_time

        out["DeleteTime"] = (
            aws_sdk_network_firewall.types.delete_time.serialize_aws_json_1_0(
                value["delete_time"]
            )
        )
    if "update_time" in value:
        import aws_sdk_network_firewall.types.update_time

        out["UpdateTime"] = (
            aws_sdk_network_firewall.types.update_time.serialize_aws_json_1_0(
                value["update_time"]
            )
        )
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "proxy_state" in value:
        import aws_sdk_network_firewall.types.proxy_state

        out["ProxyState"] = (
            aws_sdk_network_firewall.types.proxy_state.serialize_aws_json_1_0(
                value["proxy_state"]
            )
        )
    if "proxy_modify_state" in value:
        import aws_sdk_network_firewall.types.proxy_modify_state

        out["ProxyModifyState"] = (
            aws_sdk_network_firewall.types.proxy_modify_state.serialize_aws_json_1_0(
                value["proxy_modify_state"]
            )
        )
    if "nat_gateway_id" in value:
        out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    if "listener_properties" in value:
        import aws_sdk_network_firewall.types.listener_properties

        out["ListenerProperties"] = (
            aws_sdk_network_firewall.types.listener_properties.serialize_aws_json_1_0(
                value["listener_properties"]
            )
        )
    if "tls_intercept_properties" in value:
        import aws_sdk_network_firewall.types.tls_intercept_properties

        out["TlsInterceptProperties"] = (
            aws_sdk_network_firewall.types.tls_intercept_properties.serialize_aws_json_1_0(
                value["tls_intercept_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Proxy:
    out: Proxy = {}  # type: ignore[typeddict-item]
    if "CreateTime" in data:
        import aws_sdk_network_firewall.types.create_time

        out["create_time"] = (
            aws_sdk_network_firewall.types.create_time.deserialize_aws_json_1_0(
                data["CreateTime"]
            )
        )
    if "DeleteTime" in data:
        import aws_sdk_network_firewall.types.delete_time

        out["delete_time"] = (
            aws_sdk_network_firewall.types.delete_time.deserialize_aws_json_1_0(
                data["DeleteTime"]
            )
        )
    if "UpdateTime" in data:
        import aws_sdk_network_firewall.types.update_time

        out["update_time"] = (
            aws_sdk_network_firewall.types.update_time.deserialize_aws_json_1_0(
                data["UpdateTime"]
            )
        )
    if "FailureCode" in data:
        out["failure_code"] = data["FailureCode"]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "ProxyState" in data:
        import aws_sdk_network_firewall.types.proxy_state

        out["proxy_state"] = (
            aws_sdk_network_firewall.types.proxy_state.deserialize_aws_json_1_0(
                data["ProxyState"]
            )
        )
    if "ProxyModifyState" in data:
        import aws_sdk_network_firewall.types.proxy_modify_state

        out["proxy_modify_state"] = (
            aws_sdk_network_firewall.types.proxy_modify_state.deserialize_aws_json_1_0(
                data["ProxyModifyState"]
            )
        )
    if "NatGatewayId" in data:
        out["nat_gateway_id"] = data["NatGatewayId"]
    if "ProxyConfigurationName" in data:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if "ProxyConfigurationArn" in data:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    if "ProxyName" in data:
        out["proxy_name"] = data["ProxyName"]
    if "ProxyArn" in data:
        out["proxy_arn"] = data["ProxyArn"]
    if "ListenerProperties" in data:
        import aws_sdk_network_firewall.types.listener_properties

        out["listener_properties"] = (
            aws_sdk_network_firewall.types.listener_properties.deserialize_aws_json_1_0(
                data["ListenerProperties"]
            )
        )
    if "TlsInterceptProperties" in data:
        import aws_sdk_network_firewall.types.tls_intercept_properties

        out["tls_intercept_properties"] = (
            aws_sdk_network_firewall.types.tls_intercept_properties.deserialize_aws_json_1_0(
                data["TlsInterceptProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
