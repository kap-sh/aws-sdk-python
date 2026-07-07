"""Generated from Smithy shape ``com.amazonaws.redshift#RecommendedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.recommended_action_type
    import aws_sdk_redshift.types.string


class RecommendedAction(TypedDict, closed=True):
    text: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The specific instruction about the command.</p>"""
    database: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The database name to perform the action on. Only applicable if the type of command is SQL.</p>"""
    command: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The command to run.</p>"""
    type: NotRequired[
        "aws_sdk_redshift.types.recommended_action_type.RecommendedActionType"
    ]
    """<p>The type of command.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "text" in value:
        pairs.append((f"{prefix}.Text", str(value["text"])))
    if "database" in value:
        pairs.append((f"{prefix}.Database", str(value["database"])))
    if "command" in value:
        pairs.append((f"{prefix}.Command", str(value["command"])))
    if "type" in value:
        import aws_sdk_redshift.types.recommended_action_type

        aws_sdk_redshift.types.recommended_action_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )


def deserialize_query(el: Element) -> RecommendedAction:
    out: RecommendedAction = {}  # type: ignore[typeddict-item]
    child_text = el.find("Text")
    if child_text is not None:
        out["text"] = str(child_text.text or "")
    child_database = el.find("Database")
    if child_database is not None:
        out["database"] = str(child_database.text or "")
    child_command = el.find("Command")
    if child_command is not None:
        out["command"] = str(child_command.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_redshift.types.recommended_action_type

        out["type"] = aws_sdk_redshift.types.recommended_action_type.deserialize_query(
            child_type
        )
    return out
