"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncounterContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.sensitive_markdown_string


class EncounterContext(TypedDict):
    unstructured_context: NotRequired[
        "aws_sdk_connecthealth.types.sensitive_markdown_string.SensitiveMarkdownString"
    ]
    """<p>Unstructured context information in markdown format</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncounterContext) -> dict:
    out: dict = {}
    if "unstructured_context" in value:
        out["unstructuredContext"] = value["unstructured_context"]
    return out


def deserialize_json(data: dict) -> EncounterContext:
    out: EncounterContext = {}  # type: ignore[typeddict-item]
    if "unstructuredContext" in data:
        out["unstructured_context"] = data["unstructuredContext"]
    return out
