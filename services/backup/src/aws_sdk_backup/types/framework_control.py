"""Generated from Smithy shape ``com.amazonaws.backup#FrameworkControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.control_input_parameters
    import aws_sdk_backup.types.control_name
    import aws_sdk_backup.types.control_scope


class FrameworkControl(TypedDict):
    control_name: "aws_sdk_backup.types.control_name.ControlName"
    """<p>The name of a control. This name is between 1 and 256 characters.</p>"""
    control_input_parameters: NotRequired[
        "aws_sdk_backup.types.control_input_parameters.ControlInputParameters"
    ]
    """<p>The name/value pairs.</p>"""
    control_scope: NotRequired["aws_sdk_backup.types.control_scope.ControlScope"]
    r"""<p>The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html\"> <code>ControlScope</code>.</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkControl) -> dict:
    out: dict = {}
    out["ControlName"] = value["control_name"]
    if "control_input_parameters" in value:
        import aws_sdk_backup.types.control_input_parameters

        out["ControlInputParameters"] = (
            aws_sdk_backup.types.control_input_parameters.serialize_json(
                value["control_input_parameters"]
            )
        )
    if "control_scope" in value:
        import aws_sdk_backup.types.control_scope

        out["ControlScope"] = aws_sdk_backup.types.control_scope.serialize_json(
            value["control_scope"]
        )
    return out


def deserialize_json(data: dict) -> FrameworkControl:
    out: FrameworkControl = {}  # type: ignore[typeddict-item]
    if "ControlName" in data:
        out["control_name"] = data["ControlName"]
    else:
        raise DeserializationError("FrameworkControl.control_name required")
    if "ControlInputParameters" in data:
        import aws_sdk_backup.types.control_input_parameters

        out["control_input_parameters"] = (
            aws_sdk_backup.types.control_input_parameters.deserialize_json(
                data["ControlInputParameters"]
            )
        )
    if "ControlScope" in data:
        import aws_sdk_backup.types.control_scope

        out["control_scope"] = aws_sdk_backup.types.control_scope.deserialize_json(
            data["ControlScope"]
        )
    return out
