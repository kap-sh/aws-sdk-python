"""Generated from Smithy shape ``com.amazonaws.glue#GetGlueIdentityCenterConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.application_arn
    import capo_glue.types.identity_center_instance_arn
    import capo_glue.types.nullable_boolean
    import capo_glue.types.orchestration_string_list


class GetGlueIdentityCenterConfigurationResponse(TypedDict, closed=True):
    application_arn: NotRequired["capo_glue.types.application_arn.ApplicationArn"]
    """<p>The Amazon Resource Name (ARN) of the Identity Center application associated with the Glue configuration.</p>"""
    instance_arn: NotRequired[
        "capo_glue.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Identity Center instance associated with the Glue configuration.</p>"""
    scopes: NotRequired[
        "capo_glue.types.orchestration_string_list.OrchestrationStringList"
    ]
    """<p>A list of Identity Center scopes that define the permissions and access levels for the Glue configuration.</p>"""
    user_background_sessions_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether users can run background sessions when using Identity Center authentication with Glue services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGlueIdentityCenterConfigurationResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "scopes" in value:
        import capo_glue.types.orchestration_string_list

        out["Scopes"] = (
            capo_glue.types.orchestration_string_list.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    if "user_background_sessions_enabled" in value:
        out["UserBackgroundSessionsEnabled"] = value["user_background_sessions_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGlueIdentityCenterConfigurationResponse:
    out: GetGlueIdentityCenterConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "Scopes" in data:
        import capo_glue.types.orchestration_string_list

        out["scopes"] = (
            capo_glue.types.orchestration_string_list.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    if "UserBackgroundSessionsEnabled" in data:
        out["user_background_sessions_enabled"] = data["UserBackgroundSessionsEnabled"]
    return out
