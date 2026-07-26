"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#EndpointAccessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.endpoint_access

EndpointAccessList: TypeAlias = list[
    "capo_redshift_serverless.types.endpoint_access.EndpointAccess"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointAccessList) -> list:
    import capo_redshift_serverless.types.endpoint_access

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.endpoint_access.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointAccessList:
    import capo_redshift_serverless.types.endpoint_access

    out: EndpointAccessList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.endpoint_access.deserialize_aws_json_1_1(
                item
            )
        )
    return out
