"""Generated from Smithy shape ``com.amazonaws.glue#OAuth2ClientApplication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.aws_managed_client_application_reference
    import aws_sdk_glue.types.user_managed_client_application_client_id


class OAuth2ClientApplication(TypedDict):
    user_managed_client_application_client_id: NotRequired[
        "aws_sdk_glue.types.user_managed_client_application_client_id.UserManagedClientApplicationClientId"
    ]
    """<p>The client application clientID if the ClientAppType is <code>USER_MANAGED</code>.</p>"""
    aws_managed_client_application_reference: NotRequired[
        "aws_sdk_glue.types.aws_managed_client_application_reference.AWSManagedClientApplicationReference"
    ]
    """<p>The reference to the SaaS-side client app that is Amazon Web Services managed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuth2ClientApplication) -> dict:
    out: dict = {}
    if "user_managed_client_application_client_id" in value:
        out["UserManagedClientApplicationClientId"] = value[
            "user_managed_client_application_client_id"
        ]
    if "aws_managed_client_application_reference" in value:
        out["AWSManagedClientApplicationReference"] = value[
            "aws_managed_client_application_reference"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> OAuth2ClientApplication:
    out: OAuth2ClientApplication = {}  # type: ignore[typeddict-item]
    if "UserManagedClientApplicationClientId" in data:
        out["user_managed_client_application_client_id"] = data[
            "UserManagedClientApplicationClientId"
        ]
    if "AWSManagedClientApplicationReference" in data:
        out["aws_managed_client_application_reference"] = data[
            "AWSManagedClientApplicationReference"
        ]
    return out
