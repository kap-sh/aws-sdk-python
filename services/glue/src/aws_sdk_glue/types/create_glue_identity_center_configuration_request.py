"""Generated from Smithy shape ``com.amazonaws.glue#CreateGlueIdentityCenterConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.identity_center_instance_arn
    import aws_sdk_glue.types.identity_center_scopes_list
    import aws_sdk_glue.types.nullable_boolean


class CreateGlueIdentityCenterConfigurationRequest(TypedDict, closed=True):
    instance_arn: (
        "aws_sdk_glue.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Identity Center instance to be associated with the Glue configuration.</p>"""
    scopes: NotRequired[
        "aws_sdk_glue.types.identity_center_scopes_list.IdentityCenterScopesList"
    ]
    """<p>A list of Identity Center scopes that define the permissions and access levels for the Glue configuration.</p>"""
    user_background_sessions_enabled: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether users can run background sessions when using Identity Center authentication with Glue services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGlueIdentityCenterConfigurationRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
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
) -> CreateGlueIdentityCenterConfigurationRequest:
    out: CreateGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "CreateGlueIdentityCenterConfigurationRequest.instance_arn required"
        )
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
