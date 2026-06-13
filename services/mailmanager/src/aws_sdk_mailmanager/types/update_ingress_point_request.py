"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateIngressPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_point_configuration
    import aws_sdk_mailmanager.types.ingress_point_id
    import aws_sdk_mailmanager.types.ingress_point_name
    import aws_sdk_mailmanager.types.ingress_point_status_to_update
    import aws_sdk_mailmanager.types.rule_set_id
    import aws_sdk_mailmanager.types.tls_policy
    import aws_sdk_mailmanager.types.traffic_policy_id


class UpdateIngressPointRequest(TypedDict):
    ingress_point_id: "aws_sdk_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The identifier for the ingress endpoint you want to update.</p>"""
    ingress_point_name: NotRequired[
        "aws_sdk_mailmanager.types.ingress_point_name.IngressPointName"
    ]
    """<p>A user friendly name for the ingress endpoint resource.</p>"""
    status_to_update: NotRequired[
        "aws_sdk_mailmanager.types.ingress_point_status_to_update.IngressPointStatusToUpdate"
    ]
    """<p>The update status of an ingress endpoint.</p>"""
    rule_set_id: NotRequired["aws_sdk_mailmanager.types.rule_set_id.RuleSetId"]
    """<p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>"""
    traffic_policy_id: NotRequired[
        "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    ]
    """<p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>"""
    ingress_point_configuration: NotRequired[
        "aws_sdk_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
    ]
    """<p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>"""
    tls_policy: NotRequired["aws_sdk_mailmanager.types.tls_policy.TlsPolicy"]
    """<p>The Transport Layer Security (TLS) policy for the ingress point. Valid values are REQUIRED, OPTIONAL. Only ingress endpoints using REQUIRED or OPTIONAL as TlsPolicy can be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateIngressPointRequest) -> dict:
    out: dict = {}
    out["IngressPointId"] = value["ingress_point_id"]
    if "ingress_point_name" in value:
        out["IngressPointName"] = value["ingress_point_name"]
    if "status_to_update" in value:
        import aws_sdk_mailmanager.types.ingress_point_status_to_update

        out["StatusToUpdate"] = (
            aws_sdk_mailmanager.types.ingress_point_status_to_update.serialize_aws_json_1_0(
                value["status_to_update"]
            )
        )
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "traffic_policy_id" in value:
        out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "ingress_point_configuration" in value:
        import aws_sdk_mailmanager.types.ingress_point_configuration

        out["IngressPointConfiguration"] = (
            aws_sdk_mailmanager.types.ingress_point_configuration.serialize_aws_json_1_0(
                value["ingress_point_configuration"]
            )
        )
    if "tls_policy" in value:
        import aws_sdk_mailmanager.types.tls_policy

        out["TlsPolicy"] = aws_sdk_mailmanager.types.tls_policy.serialize_aws_json_1_0(
            value["tls_policy"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateIngressPointRequest:
    out: UpdateIngressPointRequest = {}  # type: ignore[typeddict-item]
    if "IngressPointId" in data:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        raise DeserializationError(
            "UpdateIngressPointRequest.ingress_point_id required"
        )
    if "IngressPointName" in data:
        out["ingress_point_name"] = data["IngressPointName"]
    if "StatusToUpdate" in data:
        import aws_sdk_mailmanager.types.ingress_point_status_to_update

        out["status_to_update"] = (
            aws_sdk_mailmanager.types.ingress_point_status_to_update.deserialize_aws_json_1_0(
                data["StatusToUpdate"]
            )
        )
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    if "TrafficPolicyId" in data:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    if "IngressPointConfiguration" in data:
        import aws_sdk_mailmanager.types.ingress_point_configuration

        out["ingress_point_configuration"] = (
            aws_sdk_mailmanager.types.ingress_point_configuration.deserialize_aws_json_1_0(
                data["IngressPointConfiguration"]
            )
        )
    if "TlsPolicy" in data:
        import aws_sdk_mailmanager.types.tls_policy

        out["tls_policy"] = (
            aws_sdk_mailmanager.types.tls_policy.deserialize_aws_json_1_0(
                data["TlsPolicy"]
            )
        )
    return out
