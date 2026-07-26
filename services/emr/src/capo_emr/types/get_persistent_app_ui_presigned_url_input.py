"""Generated from Smithy shape ``com.amazonaws.emr#GetPersistentAppUIPresignedURLInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.boolean_object
    import capo_emr.types.persistent_app_ui_type
    import capo_emr.types.xml_string_max_len256


class GetPersistentAppUIPresignedURLInput(TypedDict, closed=True):
    persistent_app_ui_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The persistent application user interface ID associated with the presigned URL.</p>"""
    persistent_app_ui_type: NotRequired[
        "capo_emr.types.persistent_app_ui_type.PersistentAppUIType"
    ]
    """<p>The persistent application user interface type associated with the presigned URL.</p>"""
    application_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The application ID associated with the presigned URL.</p>"""
    auth_proxy_call: NotRequired["capo_emr.types.boolean_object.BooleanObject"]
    """<p>A boolean that represents if the caller is an authentication proxy call.</p>"""
    execution_role_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The execution role ARN associated with the presigned URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPersistentAppUIPresignedURLInput) -> dict:
    out: dict = {}
    if "persistent_app_ui_id" in value:
        out["PersistentAppUIId"] = value["persistent_app_ui_id"]
    if "persistent_app_ui_type" in value:
        import capo_emr.types.persistent_app_ui_type

        out["PersistentAppUIType"] = (
            capo_emr.types.persistent_app_ui_type.serialize_aws_json_1_1(
                value["persistent_app_ui_type"]
            )
        )
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "auth_proxy_call" in value:
        out["AuthProxyCall"] = value["auth_proxy_call"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPersistentAppUIPresignedURLInput:
    out: GetPersistentAppUIPresignedURLInput = {}  # type: ignore[typeddict-item]
    if "PersistentAppUIId" in data:
        out["persistent_app_ui_id"] = data["PersistentAppUIId"]
    if "PersistentAppUIType" in data:
        import capo_emr.types.persistent_app_ui_type

        out["persistent_app_ui_type"] = (
            capo_emr.types.persistent_app_ui_type.deserialize_aws_json_1_1(
                data["PersistentAppUIType"]
            )
        )
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "AuthProxyCall" in data:
        out["auth_proxy_call"] = data["AuthProxyCall"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    return out
