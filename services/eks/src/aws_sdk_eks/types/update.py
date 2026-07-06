"""Generated from Smithy shape ``com.amazonaws.eks#Update``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.error_details
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.timestamp
    import aws_sdk_eks.types.update_params
    import aws_sdk_eks.types.update_status
    import aws_sdk_eks.types.update_type


class Update(TypedDict, closed=True):
    id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A UUID that is used to track the update.</p>"""
    status: NotRequired["aws_sdk_eks.types.update_status.UpdateStatus"]
    """<p>The current status of the update.</p>"""
    type: NotRequired["aws_sdk_eks.types.update_type.UpdateType"]
    """<p>The type of the update.</p>"""
    params: NotRequired["aws_sdk_eks.types.update_params.UpdateParams"]
    """<p>A key-value map that contains the parameters associated with the update.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    errors: NotRequired["aws_sdk_eks.types.error_details.ErrorDetails"]
    """<p>Any errors associated with a <code>Failed</code> update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Update) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        import aws_sdk_eks.types.update_status

        out["status"] = aws_sdk_eks.types.update_status.serialize_json(value["status"])
    if "type" in value:
        import aws_sdk_eks.types.update_type

        out["type"] = aws_sdk_eks.types.update_type.serialize_json(value["type"])
    if "params" in value:
        import aws_sdk_eks.types.update_params

        out["params"] = aws_sdk_eks.types.update_params.serialize_json(value["params"])
    if "created_at" in value:
        import aws_sdk_eks.types.timestamp

        out["createdAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "errors" in value:
        import aws_sdk_eks.types.error_details

        out["errors"] = aws_sdk_eks.types.error_details.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> Update:
    out: Update = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        import aws_sdk_eks.types.update_status

        out["status"] = aws_sdk_eks.types.update_status.deserialize_json(data["status"])
    if "type" in data:
        import aws_sdk_eks.types.update_type

        out["type"] = aws_sdk_eks.types.update_type.deserialize_json(data["type"])
    if "params" in data:
        import aws_sdk_eks.types.update_params

        out["params"] = aws_sdk_eks.types.update_params.deserialize_json(data["params"])
    if "createdAt" in data:
        import aws_sdk_eks.types.timestamp

        out["created_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "errors" in data:
        import aws_sdk_eks.types.error_details

        out["errors"] = aws_sdk_eks.types.error_details.deserialize_json(data["errors"])
    return out
