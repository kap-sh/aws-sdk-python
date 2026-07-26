"""Generated from Smithy shape ``com.amazonaws.emrcontainers#LakeFormationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.iam_role_arn
    import capo_emr_containers.types.secure_namespace_info
    import capo_emr_containers.types.session_tag_value


class LakeFormationConfiguration(TypedDict, closed=True):
    authorized_session_tag_value: NotRequired[
        "capo_emr_containers.types.session_tag_value.SessionTagValue"
    ]
    """<p>The session tag to authorize Amazon EMR on EKS for API calls to Lake Formation.</p>"""
    secure_namespace_info: NotRequired[
        "capo_emr_containers.types.secure_namespace_info.SecureNamespaceInfo"
    ]
    """<p>The namespace input of the system job.</p>"""
    query_engine_role_arn: NotRequired[
        "capo_emr_containers.types.iam_role_arn.IAMRoleArn"
    ]
    """<p>The query engine IAM role ARN that is tied to the secure Spark job. The <code>QueryEngine</code> role assumes the <code>JobExecutionRole</code> to execute all the Lake Formation calls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationConfiguration) -> dict:
    out: dict = {}
    if "authorized_session_tag_value" in value:
        out["authorizedSessionTagValue"] = value["authorized_session_tag_value"]
    if "secure_namespace_info" in value:
        import capo_emr_containers.types.secure_namespace_info

        out["secureNamespaceInfo"] = (
            capo_emr_containers.types.secure_namespace_info.serialize_json(
                value["secure_namespace_info"]
            )
        )
    if "query_engine_role_arn" in value:
        out["queryEngineRoleArn"] = value["query_engine_role_arn"]
    return out


def deserialize_json(data: dict) -> LakeFormationConfiguration:
    out: LakeFormationConfiguration = {}  # type: ignore[typeddict-item]
    if "authorizedSessionTagValue" in data:
        out["authorized_session_tag_value"] = data["authorizedSessionTagValue"]
    if "secureNamespaceInfo" in data:
        import capo_emr_containers.types.secure_namespace_info

        out["secure_namespace_info"] = (
            capo_emr_containers.types.secure_namespace_info.deserialize_json(
                data["secureNamespaceInfo"]
            )
        )
    if "queryEngineRoleArn" in data:
        out["query_engine_role_arn"] = data["queryEngineRoleArn"]
    return out
