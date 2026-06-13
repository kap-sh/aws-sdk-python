"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetNamespaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace


class GetNamespaceResponse(TypedDict):
    namespace: "aws_sdk_redshift_serverless.types.namespace.Namespace"
    """<p>The returned namespace object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamespaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.namespace

    out["namespace"] = (
        aws_sdk_redshift_serverless.types.namespace.serialize_aws_json_1_1(
            value["namespace"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamespaceResponse:
    out: GetNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    else:
        raise DeserializationError("GetNamespaceResponse.namespace required")
    return out
