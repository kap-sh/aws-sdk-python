"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.identity_store
    import capo_quicksight.types.namespace
    import capo_quicksight.types.namespace_status
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class CreateNamespaceResponse(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the Quick Sight namespace you created. </p>"""
    name: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The name of the new namespace that you created.</p>"""
    capacity_region: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services Region; that you want to use for the free SPICE capacity for the new namespace. This is set to the region that you run CreateNamespace in. </p>"""
    creation_status: NotRequired[
        "capo_quicksight.types.namespace_status.NamespaceStatus"
    ]
    """<p>The status of the creation of the namespace. This is an asynchronous process. A status of <code>CREATED</code> means that your namespace is ready to use. If an error occurs, it indicates if the process is <code>retryable</code> or <code>non-retryable</code>. In the case of a non-retryable error, refer to the error message for follow-up tasks.</p>"""
    identity_store: NotRequired["capo_quicksight.types.identity_store.IdentityStore"]
    """<p>Specifies the type of your user identity directory. Currently, this supports users with an identity type of <code>QUICKSIGHT</code>.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNamespaceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "capacity_region" in value:
        out["CapacityRegion"] = value["capacity_region"]
    if "creation_status" in value:
        import capo_quicksight.types.namespace_status

        out["CreationStatus"] = capo_quicksight.types.namespace_status.serialize_json(
            value["creation_status"]
        )
    if "identity_store" in value:
        import capo_quicksight.types.identity_store

        out["IdentityStore"] = capo_quicksight.types.identity_store.serialize_json(
            value["identity_store"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateNamespaceResponse:
    out: CreateNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CapacityRegion" in data:
        out["capacity_region"] = data["CapacityRegion"]
    if "CreationStatus" in data:
        import capo_quicksight.types.namespace_status

        out["creation_status"] = (
            capo_quicksight.types.namespace_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "IdentityStore" in data:
        import capo_quicksight.types.identity_store

        out["identity_store"] = capo_quicksight.types.identity_store.deserialize_json(
            data["IdentityStore"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
