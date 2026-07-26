"""Generated from Smithy shape ``com.amazonaws.mailmanager#Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.sender_ip_address
    import capo_mailmanager.types.traffic_policy_id


class Metadata(TypedDict, closed=True):
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the email was received.</p>"""
    ingress_point_id: NotRequired[
        "capo_mailmanager.types.ingress_point_id.IngressPointId"
    ]
    """<p>The ID of the ingress endpoint through which the email was received.</p>"""
    traffic_policy_id: NotRequired[
        "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    ]
    """<p>The ID of the traffic policy that was in effect when the email was received.</p>"""
    rule_set_id: NotRequired["capo_mailmanager.types.rule_set_id.RuleSetId"]
    """<p>The ID of the rule set that processed the email.</p>"""
    sender_hostname: NotRequired["str"]
    """<p>The name of the host from which the email was received.</p>"""
    sender_ip_address: NotRequired[
        "capo_mailmanager.types.sender_ip_address.SenderIpAddress"
    ]
    """<p>The IP address of the host from which the email was received.</p>"""
    tls_cipher_suite: NotRequired["str"]
    """<p>The TLS cipher suite used to communicate with the host from which the email was received.</p>"""
    tls_protocol: NotRequired["str"]
    """<p>The TLS protocol used to communicate with the host from which the email was received.</p>"""
    sending_method: NotRequired["str"]
    """<p>The name of the API call used when sent through a configuration set with archiving enabled.</p>"""
    source_identity: NotRequired["str"]
    """<p>The identity name used to authorize the sending action when sent through a configuration set with archiving enabled.</p>"""
    sending_pool: NotRequired["str"]
    """<p>The name of the dedicated IP pool used when sent through a configuration set with archiving enabled.</p>"""
    configuration_set: NotRequired["str"]
    """<p>The name of the configuration set used when sent through a configuration set with archiving enabled.</p>"""
    source_arn: NotRequired["str"]
    """<p>Specifies the archived email source, identified by either a Rule Set's ARN with an Archive action, or a Configuration Set's Archive ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Metadata) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["Timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["timestamp"]
            )
        )
    if "ingress_point_id" in value:
        out["IngressPointId"] = value["ingress_point_id"]
    if "traffic_policy_id" in value:
        out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "sender_hostname" in value:
        out["SenderHostname"] = value["sender_hostname"]
    if "sender_ip_address" in value:
        out["SenderIpAddress"] = value["sender_ip_address"]
    if "tls_cipher_suite" in value:
        out["TlsCipherSuite"] = value["tls_cipher_suite"]
    if "tls_protocol" in value:
        out["TlsProtocol"] = value["tls_protocol"]
    if "sending_method" in value:
        out["SendingMethod"] = value["sending_method"]
    if "source_identity" in value:
        out["SourceIdentity"] = value["source_identity"]
    if "sending_pool" in value:
        out["SendingPool"] = value["sending_pool"]
    if "configuration_set" in value:
        out["ConfigurationSet"] = value["configuration_set"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Metadata:
    out: Metadata = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import capo_mailmanager.types._prelude.timestamp

        out["timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["Timestamp"]
            )
        )
    if "IngressPointId" in data:
        out["ingress_point_id"] = data["IngressPointId"]
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    if "SenderHostname" in data:
        out["sender_hostname"] = data["SenderHostname"]
    if "SenderIpAddress" in data:
        out["sender_ip_address"] = data["SenderIpAddress"]
    if "TlsCipherSuite" in data:
        out["tls_cipher_suite"] = data["TlsCipherSuite"]
    if "TlsProtocol" in data:
        out["tls_protocol"] = data["TlsProtocol"]
    if "SendingMethod" in data:
        out["sending_method"] = data["SendingMethod"]
    if "SourceIdentity" in data:
        out["source_identity"] = data["SourceIdentity"]
    if "SendingPool" in data:
        out["sending_pool"] = data["SendingPool"]
    if "ConfigurationSet" in data:
        out["configuration_set"] = data["ConfigurationSet"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    return out
