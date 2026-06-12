"""Generated from Smithy shape ``com.amazonaws.emrserverless#IdentityCenterConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.identity_center_instance_arn


class IdentityCenterConfigurationInput(TypedDict):
    identity_center_instance_arn: NotRequired[
        "aws_sdk_emr_serverless.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """<p>The ARN of the IAM Identity Center instance.</p>"""
    user_background_sessions_enabled: NotRequired["bool"]
    """<p>Enables user background sessions for this application so Livy sessions can continue running after users log out of their interactive notebook or their Identity Center sessions expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterConfigurationInput) -> dict:
    out: dict = {}
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "user_background_sessions_enabled" in value:
        out["userBackgroundSessionsEnabled"] = value["user_background_sessions_enabled"]
    return out


def deserialize_json(data: dict) -> IdentityCenterConfigurationInput:
    out: IdentityCenterConfigurationInput = {}  # type: ignore[typeddict-item]
    if "identityCenterInstanceArn" in data:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    if "userBackgroundSessionsEnabled" in data:
        out["user_background_sessions_enabled"] = data["userBackgroundSessionsEnabled"]
    return out
