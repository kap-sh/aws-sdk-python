"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.namespace


class GetNamespaceResponse(TypedDict, closed=True):
    namespace: NotRequired["aws_sdk_servicediscovery.types.namespace.Namespace"]
    """<p>A complex type that contains information about the specified namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        import aws_sdk_servicediscovery.types.namespace

        out["Namespace"] = (
            aws_sdk_servicediscovery.types.namespace.serialize_aws_json_1_1(
                value["namespace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamespaceResponse:
    out: GetNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        import aws_sdk_servicediscovery.types.namespace

        out["namespace"] = (
            aws_sdk_servicediscovery.types.namespace.deserialize_aws_json_1_1(
                data["Namespace"]
            )
        )
    return out
