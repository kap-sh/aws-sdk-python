"""Generated from Smithy shape ``com.amazonaws.odb#OciIamRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.oci_iam_role

OciIamRoleList: TypeAlias = list["aws_sdk_odb.types.oci_iam_role.OciIamRole"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciIamRoleList) -> list:
    import aws_sdk_odb.types.oci_iam_role

    out: list = []
    for item in value:
        out.append(aws_sdk_odb.types.oci_iam_role.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> OciIamRoleList:
    import aws_sdk_odb.types.oci_iam_role

    out: OciIamRoleList = []
    for item in data:
        out.append(aws_sdk_odb.types.oci_iam_role.deserialize_aws_json_1_0(item))
    return out
