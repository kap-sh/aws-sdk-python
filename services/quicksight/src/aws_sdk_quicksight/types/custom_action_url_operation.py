"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomActionURLOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.url_operation_template
    import aws_sdk_quicksight.types.url_target_configuration


class CustomActionURLOperation(TypedDict, closed=True):
    url_template: "aws_sdk_quicksight.types.url_operation_template.URLOperationTemplate"
    """<p>THe URL link of the <code>CustomActionURLOperation</code>.</p>"""
    url_target: (
        "aws_sdk_quicksight.types.url_target_configuration.URLTargetConfiguration"
    )
    """<p>The target of the <code>CustomActionURLOperation</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>NEW_TAB</code>: Opens the target URL in a new browser tab.</p> </li> <li> <p> <code>NEW_WINDOW</code>: Opens the target URL in a new browser window.</p> </li> <li> <p> <code>SAME_TAB</code>: Opens the target URL in the same browser tab.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionURLOperation) -> dict:
    out: dict = {}
    out["URLTemplate"] = value["url_template"]
    import aws_sdk_quicksight.types.url_target_configuration

    out["URLTarget"] = aws_sdk_quicksight.types.url_target_configuration.serialize_json(
        value["url_target"]
    )
    return out


def deserialize_json(data: dict) -> CustomActionURLOperation:
    out: CustomActionURLOperation = {}  # type: ignore[typeddict-item]
    if "URLTemplate" in data:
        out["url_template"] = data["URLTemplate"]
    else:
        raise DeserializationError("CustomActionURLOperation.url_template required")
    if "URLTarget" in data:
        import aws_sdk_quicksight.types.url_target_configuration

        out["url_target"] = (
            aws_sdk_quicksight.types.url_target_configuration.deserialize_json(
                data["URLTarget"]
            )
        )
    else:
        raise DeserializationError("CustomActionURLOperation.url_target required")
    return out
