"""Generated from Smithy shape ``com.amazonaws.route53domains#CheckDomainTransferabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_transferability
    import aws_sdk_route_53_domains.types.message


class CheckDomainTransferabilityResponse(TypedDict, closed=True):
    transferability: NotRequired[
        "aws_sdk_route_53_domains.types.domain_transferability.DomainTransferability"
    ]
    """<p>A complex type that contains information about whether the specified domain can be transferred to Route 53.</p>"""
    message: NotRequired["aws_sdk_route_53_domains.types.message.Message"]
    """<p>Provides an explanation for when a domain can't be transferred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckDomainTransferabilityResponse) -> dict:
    out: dict = {}
    if "transferability" in value:
        import aws_sdk_route_53_domains.types.domain_transferability

        out["Transferability"] = (
            aws_sdk_route_53_domains.types.domain_transferability.serialize_aws_json_1_1(
                value["transferability"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckDomainTransferabilityResponse:
    out: CheckDomainTransferabilityResponse = {}  # type: ignore[typeddict-item]
    if "Transferability" in data:
        import aws_sdk_route_53_domains.types.domain_transferability

        out["transferability"] = (
            aws_sdk_route_53_domains.types.domain_transferability.deserialize_aws_json_1_1(
                data["Transferability"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
