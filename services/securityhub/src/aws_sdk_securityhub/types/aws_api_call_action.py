"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiCallAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.action_remote_ip_details
    import aws_sdk_securityhub.types.aws_api_call_action_domain_details
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsApiCallAction(TypedDict):
    api: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the API method that was issued.</p> <p>Length Constraints: 128.</p>"""
    service_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the Amazon Web Services service that the API method belongs to.</p> <p>Length Constraints: 128.</p>"""
    caller_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether the API call originated from a remote IP address (<code>remoteip</code>) or from a DNS domain (<code>domain</code>).</p>"""
    remote_ip_details: NotRequired[
        "aws_sdk_securityhub.types.action_remote_ip_details.ActionRemoteIpDetails"
    ]
    """<p>Provided if <code>CallerType</code> is <code>remoteip</code>. Provides information about the remote IP address that the API call originated from.</p>"""
    domain_details: NotRequired[
        "aws_sdk_securityhub.types.aws_api_call_action_domain_details.AwsApiCallActionDomainDetails"
    ]
    """<p>Provided if <code>CallerType</code> is <code>domain</code>. Provides information about the DNS domain that the API call originated from.</p>"""
    affected_resources: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>Identifies the resources that were affected by the API call.</p>"""
    first_seen: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that indicates when the API call was first observed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    last_seen: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that indicates when the API call was most recently observed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiCallAction) -> dict:
    out: dict = {}
    if "api" in value:
        out["Api"] = value["api"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "caller_type" in value:
        out["CallerType"] = value["caller_type"]
    if "remote_ip_details" in value:
        import aws_sdk_securityhub.types.action_remote_ip_details

        out["RemoteIpDetails"] = (
            aws_sdk_securityhub.types.action_remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    if "domain_details" in value:
        import aws_sdk_securityhub.types.aws_api_call_action_domain_details

        out["DomainDetails"] = (
            aws_sdk_securityhub.types.aws_api_call_action_domain_details.serialize_json(
                value["domain_details"]
            )
        )
    if "affected_resources" in value:
        import aws_sdk_securityhub.types.field_map

        out["AffectedResources"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["affected_resources"]
        )
    if "first_seen" in value:
        out["FirstSeen"] = value["first_seen"]
    if "last_seen" in value:
        out["LastSeen"] = value["last_seen"]
    return out


def deserialize_json(data: dict) -> AwsApiCallAction:
    out: AwsApiCallAction = {}  # type: ignore[typeddict-item]
    if "Api" in data:
        out["api"] = data["Api"]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    if "CallerType" in data:
        out["caller_type"] = data["CallerType"]
    if "RemoteIpDetails" in data:
        import aws_sdk_securityhub.types.action_remote_ip_details

        out["remote_ip_details"] = (
            aws_sdk_securityhub.types.action_remote_ip_details.deserialize_json(
                data["RemoteIpDetails"]
            )
        )
    if "DomainDetails" in data:
        import aws_sdk_securityhub.types.aws_api_call_action_domain_details

        out["domain_details"] = (
            aws_sdk_securityhub.types.aws_api_call_action_domain_details.deserialize_json(
                data["DomainDetails"]
            )
        )
    if "AffectedResources" in data:
        import aws_sdk_securityhub.types.field_map

        out["affected_resources"] = (
            aws_sdk_securityhub.types.field_map.deserialize_json(
                data["AffectedResources"]
            )
        )
    if "FirstSeen" in data:
        out["first_seen"] = data["FirstSeen"]
    if "LastSeen" in data:
        out["last_seen"] = data["LastSeen"]
    return out
