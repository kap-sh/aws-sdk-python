"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateNamespaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace


class UpdateNamespaceResponse(TypedDict):
    namespace: "aws_sdk_redshift_serverless.types.namespace.Namespace"
    """<p>A list of tag instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNamespaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.namespace

    out["namespace"] = (
        aws_sdk_redshift_serverless.types.namespace.serialize_aws_json_1_1(
            value["namespace"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNamespaceResponse:
    out: UpdateNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    else:
        raise DeserializationError("UpdateNamespaceResponse.namespace required")
    return out
