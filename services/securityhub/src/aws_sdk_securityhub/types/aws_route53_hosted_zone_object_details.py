"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneObjectDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_route53_hosted_zone_config_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsRoute53HostedZoneObjectDetails(TypedDict):
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID that Route 53 assigns to the hosted zone when you create it. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.</p>"""
    config: NotRequired[
        "aws_sdk_securityhub.types.aws_route53_hosted_zone_config_details.AwsRoute53HostedZoneConfigDetails"
    ]
    """<p> An object that includes the <code>Comment</code> element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneObjectDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "config" in value:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_config_details

        out["Config"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_config_details.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRoute53HostedZoneObjectDetails:
    out: AwsRoute53HostedZoneObjectDetails = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Config" in data:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_config_details

        out["config"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_config_details.deserialize_json(
                data["Config"]
            )
        )
    return out
