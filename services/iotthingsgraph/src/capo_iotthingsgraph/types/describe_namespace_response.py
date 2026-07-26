"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DescribeNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.arn
    import capo_iotthingsgraph.types.namespace_name
    import capo_iotthingsgraph.types.version


class DescribeNamespaceResponse(TypedDict, closed=True):
    namespace_arn: NotRequired["capo_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the namespace.</p>"""
    namespace_name: NotRequired[
        "capo_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace.</p>"""
    tracking_namespace_name: NotRequired[
        "capo_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the public namespace that the latest namespace version is tracking.</p>"""
    tracking_namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the public namespace that the latest version is tracking.</p>"""
    namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "tracking_namespace_name" in value:
        out["trackingNamespaceName"] = value["tracking_namespace_name"]
    if "tracking_namespace_version" in value:
        out["trackingNamespaceVersion"] = value["tracking_namespace_version"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNamespaceResponse:
    out: DescribeNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "trackingNamespaceName" in data:
        out["tracking_namespace_name"] = data["trackingNamespaceName"]
    if "trackingNamespaceVersion" in data:
        out["tracking_namespace_version"] = data["trackingNamespaceVersion"]
    if "namespaceVersion" in data:
        out["namespace_version"] = data["namespaceVersion"]
    return out
