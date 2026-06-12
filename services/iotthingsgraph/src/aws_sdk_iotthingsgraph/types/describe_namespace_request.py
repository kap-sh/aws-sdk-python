"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DescribeNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.namespace_name


class DescribeNamespaceRequest(TypedDict):
    namespace_name: NotRequired[
        "aws_sdk_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the user's namespace. Set this to <code>aws</code> to get the public namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNamespaceRequest) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNamespaceRequest:
    out: DescribeNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    return out
