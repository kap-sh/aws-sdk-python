"""Generated from Smithy shape ``com.amazonaws.glue#UpdateGlueIdentityCenterConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.identity_center_scopes_list
    import aws_sdk_glue.types.nullable_boolean


class UpdateGlueIdentityCenterConfigurationRequest(TypedDict, closed=True):
    scopes: NotRequired[
        "aws_sdk_glue.types.identity_center_scopes_list.IdentityCenterScopesList"
    ]
    """<p>A list of Identity Center scopes that define the updated permissions and access levels for the Glue configuration.</p>"""
    user_background_sessions_enabled: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether users can run background sessions when using Identity Center authentication with Glue services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGlueIdentityCenterConfigurationRequest) -> dict:
    out: dict = {}
    if "scopes" in value:
        import aws_sdk_glue.types.identity_center_scopes_list

        out["Scopes"] = (
            aws_sdk_glue.types.identity_center_scopes_list.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    if "user_background_sessions_enabled" in value:
        out["UserBackgroundSessionsEnabled"] = value["user_background_sessions_enabled"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateGlueIdentityCenterConfigurationRequest:
    out: UpdateGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Scopes" in data:
        import aws_sdk_glue.types.identity_center_scopes_list

        out["scopes"] = (
            aws_sdk_glue.types.identity_center_scopes_list.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    if "UserBackgroundSessionsEnabled" in data:
        out["user_background_sessions_enabled"] = data["UserBackgroundSessionsEnabled"]
    return out
