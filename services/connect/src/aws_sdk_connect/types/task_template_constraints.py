"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateConstraints``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.invisible_task_template_fields
    import aws_sdk_connect.types.read_only_task_template_fields
    import aws_sdk_connect.types.required_task_template_fields


class TaskTemplateConstraints(TypedDict):
    required_fields: NotRequired[
        "aws_sdk_connect.types.required_task_template_fields.RequiredTaskTemplateFields"
    ]
    """<p>Lists the fields that are required to be filled by agents.</p>"""
    read_only_fields: NotRequired[
        "aws_sdk_connect.types.read_only_task_template_fields.ReadOnlyTaskTemplateFields"
    ]
    """<p>Lists the fields that are read-only to agents, and cannot be edited.</p>"""
    invisible_fields: NotRequired[
        "aws_sdk_connect.types.invisible_task_template_fields.InvisibleTaskTemplateFields"
    ]
    """<p>Lists the fields that are invisible to agents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateConstraints) -> dict:
    out: dict = {}
    if "required_fields" in value:
        import aws_sdk_connect.types.required_task_template_fields

        out["RequiredFields"] = (
            aws_sdk_connect.types.required_task_template_fields.serialize_json(
                value["required_fields"]
            )
        )
    if "read_only_fields" in value:
        import aws_sdk_connect.types.read_only_task_template_fields

        out["ReadOnlyFields"] = (
            aws_sdk_connect.types.read_only_task_template_fields.serialize_json(
                value["read_only_fields"]
            )
        )
    if "invisible_fields" in value:
        import aws_sdk_connect.types.invisible_task_template_fields

        out["InvisibleFields"] = (
            aws_sdk_connect.types.invisible_task_template_fields.serialize_json(
                value["invisible_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaskTemplateConstraints:
    out: TaskTemplateConstraints = {}  # type: ignore[typeddict-item]
    if "RequiredFields" in data:
        import aws_sdk_connect.types.required_task_template_fields

        out["required_fields"] = (
            aws_sdk_connect.types.required_task_template_fields.deserialize_json(
                data["RequiredFields"]
            )
        )
    if "ReadOnlyFields" in data:
        import aws_sdk_connect.types.read_only_task_template_fields

        out["read_only_fields"] = (
            aws_sdk_connect.types.read_only_task_template_fields.deserialize_json(
                data["ReadOnlyFields"]
            )
        )
    if "InvisibleFields" in data:
        import aws_sdk_connect.types.invisible_task_template_fields

        out["invisible_fields"] = (
            aws_sdk_connect.types.invisible_task_template_fields.deserialize_json(
                data["InvisibleFields"]
            )
        )
    return out
