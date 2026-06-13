"""Generated from Smithy shape ``com.amazonaws.backup#UpdateFrameworkInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.framework_controls
    import aws_sdk_backup.types.framework_description
    import aws_sdk_backup.types.framework_name
    import aws_sdk_backup.types.string


class UpdateFrameworkInput(TypedDict):
    framework_name: "aws_sdk_backup.types.framework_name.FrameworkName"
    """<p>The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    framework_description: NotRequired[
        "aws_sdk_backup.types.framework_description.FrameworkDescription"
    ]
    """<p>An optional description of the framework with a maximum 1,024 characters.</p>"""
    framework_controls: NotRequired[
        "aws_sdk_backup.types.framework_controls.FrameworkControls"
    ]
    """<p>The controls that make up the framework. Each control in the list has a name, input parameters, and scope.</p>"""
    idempotency_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>UpdateFrameworkInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFrameworkInput) -> dict:
    out: dict = {}
    if "framework_description" in value:
        out["FrameworkDescription"] = value["framework_description"]
    if "framework_controls" in value:
        import aws_sdk_backup.types.framework_controls

        out["FrameworkControls"] = (
            aws_sdk_backup.types.framework_controls.serialize_json(
                value["framework_controls"]
            )
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_json(data: dict) -> UpdateFrameworkInput:
    out: UpdateFrameworkInput = {}  # type: ignore[typeddict-item]
    if "FrameworkDescription" in data:
        out["framework_description"] = data["FrameworkDescription"]
    if "FrameworkControls" in data:
        import aws_sdk_backup.types.framework_controls

        out["framework_controls"] = (
            aws_sdk_backup.types.framework_controls.deserialize_json(
                data["FrameworkControls"]
            )
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
