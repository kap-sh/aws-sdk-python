"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedDomainUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.expires_in_seconds
    import aws_sdk_sagemaker.types.landing_uri
    import aws_sdk_sagemaker.types.session_expiration_duration_in_seconds
    import aws_sdk_sagemaker.types.space_name
    import aws_sdk_sagemaker.types.user_profile_name


class CreatePresignedDomainUrlRequest(TypedDict):
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The name of the UserProfile to sign-in as.</p>"""
    session_expiration_duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
    ]
    """<p>The session expiration duration in seconds. This value defaults to 43200.</p>"""
    expires_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.expires_in_seconds.ExpiresInSeconds"
    ]
    """<p>The number of seconds until the pre-signed URL expires. This value defaults to 300.</p>"""
    space_name: NotRequired["aws_sdk_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    landing_uri: NotRequired["aws_sdk_sagemaker.types.landing_uri.LandingUri"]
    """<p>The landing page that the user is directed to when accessing the presigned URL. Using this value, users can access Studio or Studio Classic, even if it is not the default experience for the domain. The supported values are:</p> <ul> <li> <p> <code>studio::relative/path</code>: Directs users to the relative path in Studio.</p> </li> <li> <p> <code>app:JupyterServer:relative/path</code>: Directs users to the relative path in the Studio Classic application.</p> </li> <li> <p> <code>app:JupyterLab:relative/path</code>: Directs users to the relative path in the JupyterLab application.</p> </li> <li> <p> <code>app:RStudioServerPro:relative/path</code>: Directs users to the relative path in the RStudio application.</p> </li> <li> <p> <code>app:CodeEditor:relative/path</code>: Directs users to the relative path in the Code Editor, based on Code-OSS, Visual Studio Code - Open Source application.</p> </li> <li> <p> <code>app:Canvas:relative/path</code>: Directs users to the relative path in the Canvas application.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedDomainUrlRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "session_expiration_duration_in_seconds" in value:
        out["SessionExpirationDurationInSeconds"] = value[
            "session_expiration_duration_in_seconds"
        ]
    if "expires_in_seconds" in value:
        out["ExpiresInSeconds"] = value["expires_in_seconds"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "landing_uri" in value:
        out["LandingUri"] = value["landing_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedDomainUrlRequest:
    out: CreatePresignedDomainUrlRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "SessionExpirationDurationInSeconds" in data:
        out["session_expiration_duration_in_seconds"] = data[
            "SessionExpirationDurationInSeconds"
        ]
    if "ExpiresInSeconds" in data:
        out["expires_in_seconds"] = data["ExpiresInSeconds"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "LandingUri" in data:
        out["landing_uri"] = data["LandingUri"]
    return out
