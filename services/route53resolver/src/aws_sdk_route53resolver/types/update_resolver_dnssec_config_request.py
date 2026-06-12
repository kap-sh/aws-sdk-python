"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverDnssecConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.validation


class UpdateResolverDnssecConfigRequest(TypedDict):
    resource_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the virtual private cloud (VPC) that you're updating the DNSSEC validation status for.</p>"""
    validation: "aws_sdk_route53resolver.types.validation.Validation"
    """<p>The new value that you are specifying for DNSSEC validation for the VPC. The value can be <code>ENABLE</code> or <code>DISABLE</code>. Be aware that it can take time for a validation status change to be completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverDnssecConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_route53resolver.types.validation

    out["Validation"] = aws_sdk_route53resolver.types.validation.serialize_aws_json_1_1(
        value["validation"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverDnssecConfigRequest:
    out: UpdateResolverDnssecConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "UpdateResolverDnssecConfigRequest.resource_id required"
        )
    if "Validation" in data:
        import aws_sdk_route53resolver.types.validation

        out["validation"] = (
            aws_sdk_route53resolver.types.validation.deserialize_aws_json_1_1(
                data["Validation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateResolverDnssecConfigRequest.validation required"
        )
    return out
