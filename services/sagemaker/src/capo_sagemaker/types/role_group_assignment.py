"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoleGroupAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.group_patterns_list
    import capo_sagemaker.types.non_empty_string256


class RoleGroupAssignment(TypedDict, closed=True):
    role_name: "capo_sagemaker.types.non_empty_string256.NonEmptyString256"
    """<p>The name of the in-app role within the SageMaker Partner AI App. The specific roles available depend on the app type and version.</p>"""
    group_patterns: "capo_sagemaker.types.group_patterns_list.GroupPatternsList"
    """<p>A list of Amazon Web Services IAM Identity Center group patterns that should be assigned to the specified role. Group patterns support wildcard matching using <code>*</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoleGroupAssignment) -> dict:
    out: dict = {}
    out["RoleName"] = value["role_name"]
    import capo_sagemaker.types.group_patterns_list

    out["GroupPatterns"] = (
        capo_sagemaker.types.group_patterns_list.serialize_aws_json_1_1(
            value["group_patterns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoleGroupAssignment:
    out: RoleGroupAssignment = {}  # type: ignore[typeddict-item]
    if "RoleName" in data:
        out["role_name"] = data["RoleName"]
    else:
        raise DeserializationError("RoleGroupAssignment.role_name required")
    if "GroupPatterns" in data:
        import capo_sagemaker.types.group_patterns_list

        out["group_patterns"] = (
            capo_sagemaker.types.group_patterns_list.deserialize_aws_json_1_1(
                data["GroupPatterns"]
            )
        )
    else:
        raise DeserializationError("RoleGroupAssignment.group_patterns required")
    return out
