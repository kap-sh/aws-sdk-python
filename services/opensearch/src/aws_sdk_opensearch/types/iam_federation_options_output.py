"""Generated from Smithy shape ``com.amazonaws.opensearch#IAMFederationOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.iam_federation_roles_key
    import aws_sdk_opensearch.types.iam_federation_subject_key


class IAMFederationOptionsOutput(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether IAM identity federation is currently enabled for the domain.</p>"""
    subject_key: NotRequired[
        "aws_sdk_opensearch.types.iam_federation_subject_key.IAMFederationSubjectKey"
    ]
    """<p>The configured key in the SAML assertion for the user's subject identifier.</p>"""
    roles_key: NotRequired[
        "aws_sdk_opensearch.types.iam_federation_roles_key.IAMFederationRolesKey"
    ]
    """<p>The configured key in the SAML assertion for the user's role information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMFederationOptionsOutput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "subject_key" in value:
        out["SubjectKey"] = value["subject_key"]
    if "roles_key" in value:
        out["RolesKey"] = value["roles_key"]
    return out


def deserialize_json(data: dict) -> IAMFederationOptionsOutput:
    out: IAMFederationOptionsOutput = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "SubjectKey" in data:
        out["subject_key"] = data["SubjectKey"]
    if "RolesKey" in data:
        out["roles_key"] = data["RolesKey"]
    return out
