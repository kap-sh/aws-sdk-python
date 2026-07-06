"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteMultiRegionEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.status


class DeleteMultiRegionEndpointResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_sesv2.types.status.Status"]
    """<p>A status of the multi-region endpoint (global-endpoint) right after the delete request.</p> <ul> <li> <p> <code>CREATING</code> – The resource is being provisioned.</p> </li> <li> <p> <code>READY</code> – The resource is ready to use.</p> </li> <li> <p> <code>FAILED</code> – The resource failed to be provisioned.</p> </li> <li> <p> <code>DELETING</code> – The resource is being deleted as requested.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMultiRegionEndpointResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sesv2.types.status

        out["Status"] = aws_sdk_sesv2.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteMultiRegionEndpointResponse:
    out: DeleteMultiRegionEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sesv2.types.status

        out["status"] = aws_sdk_sesv2.types.status.deserialize_json(data["Status"])
    return out
