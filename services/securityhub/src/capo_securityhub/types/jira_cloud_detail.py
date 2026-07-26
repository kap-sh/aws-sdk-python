"""Generated from Smithy shape ``com.amazonaws.securityhub#JiraCloudDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.connector_auth_status
    import capo_securityhub.types.non_empty_string


class JiraCloudDetail(TypedDict, closed=True):
    cloud_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The cloud id of the Jira Cloud.</p>"""
    project_key: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The projectKey of Jira Cloud.</p>"""
    domain: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URL domain of your Jira Cloud instance.</p>"""
    auth_url: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URL to provide to customers for OAuth auth code flow.</p>"""
    auth_status: NotRequired[
        "capo_securityhub.types.connector_auth_status.ConnectorAuthStatus"
    ]
    """<p>The status of the authorization between Jira Cloud and the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraCloudDetail) -> dict:
    out: dict = {}
    if "cloud_id" in value:
        out["CloudId"] = value["cloud_id"]
    if "project_key" in value:
        out["ProjectKey"] = value["project_key"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "auth_url" in value:
        out["AuthUrl"] = value["auth_url"]
    if "auth_status" in value:
        import capo_securityhub.types.connector_auth_status

        out["AuthStatus"] = capo_securityhub.types.connector_auth_status.serialize_json(
            value["auth_status"]
        )
    return out


def deserialize_json(data: dict) -> JiraCloudDetail:
    out: JiraCloudDetail = {}  # type: ignore[typeddict-item]
    if "CloudId" in data:
        out["cloud_id"] = data["CloudId"]
    if "ProjectKey" in data:
        out["project_key"] = data["ProjectKey"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "AuthUrl" in data:
        out["auth_url"] = data["AuthUrl"]
    if "AuthStatus" in data:
        import capo_securityhub.types.connector_auth_status

        out["auth_status"] = (
            capo_securityhub.types.connector_auth_status.deserialize_json(
                data["AuthStatus"]
            )
        )
    return out
