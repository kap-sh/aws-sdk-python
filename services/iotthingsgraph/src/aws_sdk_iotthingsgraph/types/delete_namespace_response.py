"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeleteNamespaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.arn
    import aws_sdk_iotthingsgraph.types.namespace_name


class DeleteNamespaceResponse(TypedDict):
    namespace_arn: NotRequired["aws_sdk_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the namespace to be deleted.</p>"""
    namespace_name: NotRequired[
        "aws_sdk_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceResponse:
    out: DeleteNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    return out
