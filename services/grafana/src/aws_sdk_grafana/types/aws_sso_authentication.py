"""Generated from Smithy shape ``com.amazonaws.grafana#AwsSsoAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_grafana.types.sso_client_id


class AwsSsoAuthentication(TypedDict, closed=True):
    sso_client_id: NotRequired["aws_sdk_grafana.types.sso_client_id.SSOClientId"]
    """<p>The ID of the IAM Identity Center-managed application that is created by Amazon Managed Grafana.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSsoAuthentication) -> dict:
    out: dict = {}
    if "sso_client_id" in value:
        out["ssoClientId"] = value["sso_client_id"]
    return out


def deserialize_json(data: dict) -> AwsSsoAuthentication:
    out: AwsSsoAuthentication = {}  # type: ignore[typeddict-item]
    if "ssoClientId" in data:
        out["sso_client_id"] = data["ssoClientId"]
    return out
