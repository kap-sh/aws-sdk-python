"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdatePrivateDnsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.arn
    import aws_sdk_servicediscovery.types.private_dns_namespace_change
    import aws_sdk_servicediscovery.types.resource_id


class UpdatePrivateDnsNamespaceRequest(TypedDict, closed=True):
    id: "aws_sdk_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the namespace that you want to update.</p>"""
    updater_request_id: NotRequired[
        "aws_sdk_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>UpdatePrivateDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>UpdaterRequestId</code> can be any unique string (for example, a date/timestamp).</p>"""
    namespace: "aws_sdk_servicediscovery.types.private_dns_namespace_change.PrivateDnsNamespaceChange"
    """<p>Updated properties for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePrivateDnsNamespaceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "updater_request_id" in value:
        out["UpdaterRequestId"] = value["updater_request_id"]
    import aws_sdk_servicediscovery.types.private_dns_namespace_change

    out["Namespace"] = (
        aws_sdk_servicediscovery.types.private_dns_namespace_change.serialize_aws_json_1_1(
            value["namespace"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePrivateDnsNamespaceRequest:
    out: UpdatePrivateDnsNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdatePrivateDnsNamespaceRequest.id required")
    if "UpdaterRequestId" in data:
        out["updater_request_id"] = data["UpdaterRequestId"]
    if "Namespace" in data:
        import aws_sdk_servicediscovery.types.private_dns_namespace_change

        out["namespace"] = (
            aws_sdk_servicediscovery.types.private_dns_namespace_change.deserialize_aws_json_1_1(
                data["Namespace"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePrivateDnsNamespaceRequest.namespace required"
        )
    return out
