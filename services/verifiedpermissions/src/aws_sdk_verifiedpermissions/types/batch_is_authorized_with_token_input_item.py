"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedWithTokenInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.action_identifier
    import aws_sdk_verifiedpermissions.types.context_definition
    import aws_sdk_verifiedpermissions.types.entity_identifier


class BatchIsAuthorizedWithTokenInputItem(TypedDict, closed=True):
    action: NotRequired[
        "aws_sdk_verifiedpermissions.types.action_identifier.ActionIdentifier"
    ]
    """<p>Specifies the requested action to be authorized. For example, <code>PhotoFlash::ReadPhoto</code>.</p>"""
    resource: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>Specifies the resource that you want an authorization decision for. For example, <code>PhotoFlash::Photo</code>.</p>"""
    context: NotRequired[
        "aws_sdk_verifiedpermissions.types.context_definition.ContextDefinition"
    ]
    """<p>Specifies additional context that can be used to make more granular authorization decisions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedWithTokenInputItem) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_verifiedpermissions.types.action_identifier

        out["action"] = (
            aws_sdk_verifiedpermissions.types.action_identifier.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "resource" in value:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "context" in value:
        import aws_sdk_verifiedpermissions.types.context_definition

        out["context"] = (
            aws_sdk_verifiedpermissions.types.context_definition.serialize_aws_json_1_0(
                value["context"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedWithTokenInputItem:
    out: BatchIsAuthorizedWithTokenInputItem = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_verifiedpermissions.types.action_identifier

        out["action"] = (
            aws_sdk_verifiedpermissions.types.action_identifier.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    if "resource" in data:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if "context" in data:
        import aws_sdk_verifiedpermissions.types.context_definition

        out["context"] = (
            aws_sdk_verifiedpermissions.types.context_definition.deserialize_aws_json_1_0(
                data["context"]
            )
        )
    return out
