"""Generated from Smithy shape ``com.amazonaws.securityagent#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.application_domain
    import aws_sdk_securityagent.types.application_id
    import aws_sdk_securityagent.types.default_kms_key_id


class ApplicationSummary(TypedDict, closed=True):
    application_id: "aws_sdk_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application.</p>"""
    application_name: "str"
    """<p>The name of the application.</p>"""
    domain: "aws_sdk_securityagent.types.application_domain.ApplicationDomain"
    """<p>The domain associated with the application.</p>"""
    default_kms_key_id: NotRequired[
        "aws_sdk_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
    ]
    """<p>The identifier of the default AWS KMS key used to encrypt data for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["applicationName"] = value["application_name"]
    out["domain"] = value["domain"]
    if "default_kms_key_id" in value:
        out["defaultKmsKeyId"] = value["default_kms_key_id"]
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("ApplicationSummary.application_id required")
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError("ApplicationSummary.application_name required")
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("ApplicationSummary.domain required")
    if "defaultKmsKeyId" in data:
        out["default_kms_key_id"] = data["defaultKmsKeyId"]
    return out
