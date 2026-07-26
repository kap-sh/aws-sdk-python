"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterIamRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_iam_role

AwsRedshiftClusterIamRoles: TypeAlias = list[
    "capo_securityhub.types.aws_redshift_cluster_iam_role.AwsRedshiftClusterIamRole"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterIamRoles) -> list:
    import capo_securityhub.types.aws_redshift_cluster_iam_role

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_iam_role.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterIamRoles:
    import capo_securityhub.types.aws_redshift_cluster_iam_role

    out: AwsRedshiftClusterIamRoles = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_iam_role.deserialize_json(item)
        )
    return out
