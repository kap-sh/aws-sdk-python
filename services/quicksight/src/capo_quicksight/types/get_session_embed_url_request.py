"""Generated from Smithy shape ``com.amazonaws.quicksight#GetSessionEmbedUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.entry_point
    import capo_quicksight.types.session_lifetime_in_minutes


class GetSessionEmbedUrlRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account associated with your Amazon Quick Sight subscription.</p>"""
    entry_point: NotRequired["capo_quicksight.types.entry_point.EntryPoint"]
    """<p>The URL you use to access the embedded session. The entry point URL is constrained to the following paths:</p> <ul> <li> <p> <code>/start</code> </p> </li> <li> <p> <code>/start/analyses</code> </p> </li> <li> <p> <code>/start/dashboards</code> </p> </li> <li> <p> <code>/start/favorites</code> </p> </li> <li> <p> <code>/dashboards/<i>DashboardId</i> </code> - where <code>DashboardId</code> is the actual ID key from the Amazon Quick Sight console URL of the dashboard</p> </li> <li> <p> <code>/analyses/<i>AnalysisId</i> </code> - where <code>AnalysisId</code> is the actual ID key from the Amazon Quick Sight console URL of the analysis</p> </li> </ul>"""
    session_lifetime_in_minutes: NotRequired[
        "capo_quicksight.types.session_lifetime_in_minutes.SessionLifetimeInMinutes"
    ]
    """<p>How many minutes the session is valid. The session lifetime must be 15-600 minutes.</p>"""
    user_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Quick user's Amazon Resource Name (ARN), for use with <code>QUICKSIGHT</code> identity type. You can use this for any type of Amazon Quick users in your account (readers, authors, or admins). They need to be authenticated as one of the following:</p> <ol> <li> <p>Active Directory (AD) users or group members</p> </li> <li> <p>Invited nonfederated users</p> </li> <li> <p>IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation</p> </li> </ol> <p>Omit this parameter for users in the third group, IAM users and IAM role-based sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionEmbedUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionEmbedUrlRequest:
    out: GetSessionEmbedUrlRequest = {}  # type: ignore[typeddict-item]
    return out
