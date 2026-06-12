"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#Target``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhub_config.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.target_id
    import aws_sdk_migrationhub_config.types.target_type


class Target(TypedDict):
    type: "aws_sdk_migrationhub_config.types.target_type.TargetType"
    """<p>The target type is always an <code>ACCOUNT</code>.</p>"""
    id: NotRequired["aws_sdk_migrationhub_config.types.target_id.TargetId"]
    """<p>The <code>TargetID</code> is a 12-character identifier of the <code>ACCOUNT</code> for which the control was created. (This must be the current account.) </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Target) -> dict:
    out: dict = {}
    import aws_sdk_migrationhub_config.types.target_type

    out["Type"] = aws_sdk_migrationhub_config.types.target_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_migrationhub_config.types.target_type

        out["type"] = (
            aws_sdk_migrationhub_config.types.target_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("Target.type required")
    if "Id" in data:
        out["id"] = data["Id"]
    return out
