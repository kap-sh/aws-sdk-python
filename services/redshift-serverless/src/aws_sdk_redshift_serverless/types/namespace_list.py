"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#NamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace

NamespaceList: TypeAlias = list["aws_sdk_redshift_serverless.types.namespace.Namespace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceList) -> list:
    import aws_sdk_redshift_serverless.types.namespace

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.namespace.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NamespaceList:
    import aws_sdk_redshift_serverless.types.namespace

    out: NamespaceList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.namespace.deserialize_aws_json_1_1(item)
        )
    return out
