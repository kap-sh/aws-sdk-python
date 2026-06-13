"""Generated from Smithy shape ``com.amazonaws.backup#CreateFrameworkInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.framework_controls
    import aws_sdk_backup.types.framework_description
    import aws_sdk_backup.types.framework_name
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.string_map


class CreateFrameworkInput(TypedDict):
    framework_name: "aws_sdk_backup.types.framework_name.FrameworkName"
    """<p>The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    framework_description: NotRequired[
        "aws_sdk_backup.types.framework_description.FrameworkDescription"
    ]
    """<p>An optional description of the framework with a maximum of 1,024 characters.</p>"""
    framework_controls: "aws_sdk_backup.types.framework_controls.FrameworkControls"
    """<p>The controls that make up the framework. Each control in the list has a name, input parameters, and scope.</p>"""
    idempotency_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>CreateFrameworkInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    framework_tags: NotRequired["aws_sdk_backup.types.string_map.stringMap"]
    """<p>The tags to assign to the framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFrameworkInput) -> dict:
    out: dict = {}
    out["FrameworkName"] = value["framework_name"]
    if "framework_description" in value:
        out["FrameworkDescription"] = value["framework_description"]
    import aws_sdk_backup.types.framework_controls

    out["FrameworkControls"] = aws_sdk_backup.types.framework_controls.serialize_json(
        value["framework_controls"]
    )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "framework_tags" in value:
        import aws_sdk_backup.types.string_map

        out["FrameworkTags"] = aws_sdk_backup.types.string_map.serialize_json(
            value["framework_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFrameworkInput:
    out: CreateFrameworkInput = {}  # type: ignore[typeddict-item]
    if "FrameworkName" in data:
        out["framework_name"] = data["FrameworkName"]
    else:
        raise DeserializationError("CreateFrameworkInput.framework_name required")
    if "FrameworkDescription" in data:
        out["framework_description"] = data["FrameworkDescription"]
    if "FrameworkControls" in data:
        import aws_sdk_backup.types.framework_controls

        out["framework_controls"] = (
            aws_sdk_backup.types.framework_controls.deserialize_json(
                data["FrameworkControls"]
            )
        )
    else:
        raise DeserializationError("CreateFrameworkInput.framework_controls required")
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    if "FrameworkTags" in data:
        import aws_sdk_backup.types.string_map

        out["framework_tags"] = aws_sdk_backup.types.string_map.deserialize_json(
            data["FrameworkTags"]
        )
    return out
