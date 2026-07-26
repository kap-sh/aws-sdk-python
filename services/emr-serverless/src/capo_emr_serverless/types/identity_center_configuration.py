"""Generated from Smithy shape ``com.amazonaws.emrserverless#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.identity_center_application_arn
    import capo_emr_serverless.types.identity_center_instance_arn


class IdentityCenterConfiguration(TypedDict, closed=True):
    identity_center_instance_arn: NotRequired[
        "capo_emr_serverless.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """<p>The ARN of the IAM Identity Center instance.</p>"""
    identity_center_application_arn: NotRequired[
        "capo_emr_serverless.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The ARN of the EMR Serverless created IAM Identity Center Application that provides trusted-identity propagation.</p>"""
    user_background_sessions_enabled: NotRequired["bool"]
    """<p>Enables user background sessions for this application so Livy sessions can continue running after users log out of their interactive notebook or their Identity Center sessions expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "identity_center_application_arn" in value:
        out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    if "user_background_sessions_enabled" in value:
        out["userBackgroundSessionsEnabled"] = value["user_background_sessions_enabled"]
    return out


def deserialize_json(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if "identityCenterInstanceArn" in data:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    if "identityCenterApplicationArn" in data:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    if "userBackgroundSessionsEnabled" in data:
        out["user_background_sessions_enabled"] = data["userBackgroundSessionsEnabled"]
    return out
