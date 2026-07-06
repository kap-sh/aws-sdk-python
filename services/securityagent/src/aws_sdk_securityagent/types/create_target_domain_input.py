"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateTargetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.domain_verification_method
    import aws_sdk_securityagent.types.tag_map


class CreateTargetDomainInput(TypedDict, closed=True):
    target_domain_name: "str"
    """<p>The domain name to register as a target domain.</p>"""
    verification_method: "aws_sdk_securityagent.types.domain_verification_method.DomainVerificationMethod"
    """<p>The method to use for verifying domain ownership. Valid values are DNS_TXT, HTTP_ROUTE, and PRIVATE_VPC.</p>"""
    tags: NotRequired["aws_sdk_securityagent.types.tag_map.TagMap"]
    """<p>The tags to associate with the target domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTargetDomainInput) -> dict:
    out: dict = {}
    out["targetDomainName"] = value["target_domain_name"]
    import aws_sdk_securityagent.types.domain_verification_method

    out["verificationMethod"] = (
        aws_sdk_securityagent.types.domain_verification_method.serialize_json(
            value["verification_method"]
        )
    )
    if "tags" in value:
        import aws_sdk_securityagent.types.tag_map

        out["tags"] = aws_sdk_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTargetDomainInput:
    out: CreateTargetDomainInput = {}  # type: ignore[typeddict-item]
    if "targetDomainName" in data:
        out["target_domain_name"] = data["targetDomainName"]
    else:
        raise DeserializationError(
            "CreateTargetDomainInput.target_domain_name required"
        )
    if "verificationMethod" in data:
        import aws_sdk_securityagent.types.domain_verification_method

        out["verification_method"] = (
            aws_sdk_securityagent.types.domain_verification_method.deserialize_json(
                data["verificationMethod"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTargetDomainInput.verification_method required"
        )
    if "tags" in data:
        import aws_sdk_securityagent.types.tag_map

        out["tags"] = aws_sdk_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out
