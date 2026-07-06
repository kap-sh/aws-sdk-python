"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace


class CreateNamespaceResponse(TypedDict, closed=True):
    namespace: NotRequired["aws_sdk_redshift_serverless.types.namespace.Namespace"]
    """<p>The created namespace object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.serialize_aws_json_1_1(
                value["namespace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamespaceResponse:
    out: CreateNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    return out
