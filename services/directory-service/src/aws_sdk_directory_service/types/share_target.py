"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.target_id
    import aws_sdk_directory_service.types.target_type


class ShareTarget(TypedDict, closed=True):
    id: "aws_sdk_directory_service.types.target_id.TargetId"
    """<p>Identifier of the directory consumer account.</p>"""
    type: "aws_sdk_directory_service.types.target_type.TargetType"
    """<p>Type of identifier to be used in the <code>Id</code> field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareTarget) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_directory_service.types.target_type

    out["Type"] = aws_sdk_directory_service.types.target_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareTarget:
    out: ShareTarget = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ShareTarget.id required")
    if "Type" in data:
        import aws_sdk_directory_service.types.target_type

        out["type"] = (
            aws_sdk_directory_service.types.target_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ShareTarget.type required")
    return out
