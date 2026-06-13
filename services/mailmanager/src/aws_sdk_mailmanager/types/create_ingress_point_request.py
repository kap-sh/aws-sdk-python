"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateIngressPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.ingress_point_configuration
    import aws_sdk_mailmanager.types.ingress_point_name
    import aws_sdk_mailmanager.types.ingress_point_type
    import aws_sdk_mailmanager.types.network_configuration
    import aws_sdk_mailmanager.types.rule_set_id
    import aws_sdk_mailmanager.types.tag_list
    import aws_sdk_mailmanager.types.tls_policy
    import aws_sdk_mailmanager.types.traffic_policy_id


class CreateIngressPointRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    ingress_point_name: "aws_sdk_mailmanager.types.ingress_point_name.IngressPointName"
    """<p>A user friendly name for an ingress endpoint resource.</p>"""
    type: "aws_sdk_mailmanager.types.ingress_point_type.IngressPointType"
    """<p>The type of the ingress endpoint to create.</p>"""
    rule_set_id: "aws_sdk_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>"""
    traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>"""
    ingress_point_configuration: NotRequired[
        "aws_sdk_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
    ]
    """<p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_mailmanager.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Specifies the network configuration for the ingress point. This allows you to create an IPv4-only, Dual-Stack, or PrivateLink type of ingress point. If not specified, the default network type is IPv4-only. </p>"""
    tls_policy: NotRequired["aws_sdk_mailmanager.types.tls_policy.TlsPolicy"]
    """<p>The Transport Layer Security (TLS) policy for the ingress point. The FIPS value is only valid in US and Canada regions.</p>"""
    tags: NotRequired["aws_sdk_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngressPointRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["IngressPointName"] = value["ingress_point_name"]
    import aws_sdk_mailmanager.types.ingress_point_type

    out["Type"] = aws_sdk_mailmanager.types.ingress_point_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["RuleSetId"] = value["rule_set_id"]
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "ingress_point_configuration" in value:
        import aws_sdk_mailmanager.types.ingress_point_configuration

        out["IngressPointConfiguration"] = (
            aws_sdk_mailmanager.types.ingress_point_configuration.serialize_aws_json_1_0(
                value["ingress_point_configuration"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_mailmanager.types.network_configuration

        out["NetworkConfiguration"] = (
            aws_sdk_mailmanager.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "tls_policy" in value:
        import aws_sdk_mailmanager.types.tls_policy

        out["TlsPolicy"] = aws_sdk_mailmanager.types.tls_policy.serialize_aws_json_1_0(
            value["tls_policy"]
        )
    if "tags" in value:
        import aws_sdk_mailmanager.types.tag_list

        out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngressPointRequest:
    out: CreateIngressPointRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "IngressPointName" in data:
        out["ingress_point_name"] = data["IngressPointName"]
    else:
        raise DeserializationError(
            "CreateIngressPointRequest.ingress_point_name required"
        )
    if "Type" in data:
        import aws_sdk_mailmanager.types.ingress_point_type

        out["type"] = (
            aws_sdk_mailmanager.types.ingress_point_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CreateIngressPointRequest.type required")
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("CreateIngressPointRequest.rule_set_id required")
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        raise DeserializationError(
            "CreateIngressPointRequest.traffic_policy_id required"
        )
    if "IngressPointConfiguration" in data:
        import aws_sdk_mailmanager.types.ingress_point_configuration

        out["ingress_point_configuration"] = (
            aws_sdk_mailmanager.types.ingress_point_configuration.deserialize_aws_json_1_0(
                data["IngressPointConfiguration"]
            )
        )
    if "NetworkConfiguration" in data:
        import aws_sdk_mailmanager.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_mailmanager.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if "TlsPolicy" in data:
        import aws_sdk_mailmanager.types.tls_policy

        out["tls_policy"] = (
            aws_sdk_mailmanager.types.tls_policy.deserialize_aws_json_1_0(
                data["TlsPolicy"]
            )
        )
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
