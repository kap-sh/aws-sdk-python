"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateInstanceMetadataOptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.operation


class UpdateInstanceMetadataOptionsResult(TypedDict, closed=True):
    operation: NotRequired["aws_sdk_lightsail.types.operation.Operation"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceMetadataOptionsResult) -> dict:
    out: dict = {}
    if "operation" in value:
        import aws_sdk_lightsail.types.operation

        out["operation"] = aws_sdk_lightsail.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceMetadataOptionsResult:
    out: UpdateInstanceMetadataOptionsResult = {}  # type: ignore[typeddict-item]
    if "operation" in data:
        import aws_sdk_lightsail.types.operation

        out["operation"] = aws_sdk_lightsail.types.operation.deserialize_aws_json_1_1(
            data["operation"]
        )
    return out
