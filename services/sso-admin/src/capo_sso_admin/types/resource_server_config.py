"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ResourceServerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.resource_server_scopes


class ResourceServerConfig(TypedDict, closed=True):
    scopes: NotRequired[
        "capo_sso_admin.types.resource_server_scopes.ResourceServerScopes"
    ]
    """<p>A list of the IAM Identity Center access scopes that are associated with this resource server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServerConfig) -> dict:
    out: dict = {}
    if "scopes" in value:
        import capo_sso_admin.types.resource_server_scopes

        out["Scopes"] = (
            capo_sso_admin.types.resource_server_scopes.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceServerConfig:
    out: ResourceServerConfig = {}  # type: ignore[typeddict-item]
    if "Scopes" in data:
        import capo_sso_admin.types.resource_server_scopes

        out["scopes"] = (
            capo_sso_admin.types.resource_server_scopes.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out
