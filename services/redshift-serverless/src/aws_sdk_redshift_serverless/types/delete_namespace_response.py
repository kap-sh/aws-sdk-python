"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace


class DeleteNamespaceResponse(TypedDict, closed=True):
    namespace: "aws_sdk_redshift_serverless.types.namespace.Namespace"
    """<p>The deleted namespace object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.namespace

    out["namespace"] = (
        aws_sdk_redshift_serverless.types.namespace.serialize_aws_json_1_1(
            value["namespace"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceResponse:
    out: DeleteNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    else:
        raise DeserializationError("DeleteNamespaceResponse.namespace required")
    return out
