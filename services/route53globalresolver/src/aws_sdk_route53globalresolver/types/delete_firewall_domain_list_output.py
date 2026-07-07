"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteFirewallDomainListOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.cr_resource_status
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class DeleteFirewallDomainListOutput(TypedDict, closed=True):
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted firewall domain list.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted firewall domain list.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the deleted firewall domain list.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The final status of the deleted firewall domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFirewallDomainListOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_route53globalresolver.types.cr_resource_status

    out["status"] = (
        aws_sdk_route53globalresolver.types.cr_resource_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteFirewallDomainListOutput:
    out: DeleteFirewallDomainListOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteFirewallDomainListOutput.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteFirewallDomainListOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteFirewallDomainListOutput.name required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.cr_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteFirewallDomainListOutput.status required")
    return out
