"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.namespace_info_v2
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeNamespaceResponse(TypedDict, closed=True):
    namespace: NotRequired["capo_quicksight.types.namespace_info_v2.NamespaceInfoV2"]
    """<p>The information about the namespace that you're describing. The response includes the namespace ARN, name, Amazon Web Services Region, creation status, and identity store. <code>DescribeNamespace</code> also works for namespaces that are in the process of being created. For incomplete namespaces, this API operation lists the namespace error types and messages associated with the creation process.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        import capo_quicksight.types.namespace_info_v2

        out["Namespace"] = capo_quicksight.types.namespace_info_v2.serialize_json(
            value["namespace"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeNamespaceResponse:
    out: DescribeNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        import capo_quicksight.types.namespace_info_v2

        out["namespace"] = capo_quicksight.types.namespace_info_v2.deserialize_json(
            data["Namespace"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
