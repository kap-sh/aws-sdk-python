"""Generated from Smithy shape ``com.amazonaws.applicationsignals#SelectionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.selection_pattern
    import aws_sdk_application_signals.types.selection_type


class SelectionConfig(TypedDict):
    type: "aws_sdk_application_signals.types.selection_type.SelectionType"
    pattern: NotRequired[
        "aws_sdk_application_signals.types.selection_pattern.SelectionPattern"
    ]
    """<p>A prefix string or regular expression that specifies which operations to include in a service-level SLO. When <code>SelectionType</code> is <code>PREFIX</code>, this value is a prefix string that matches the beginning of operation names. When <code>SelectionType</code> is <code>REGEX</code>, this value is a regular expression that matches operation names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectionConfig) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.selection_type

    out["Type"] = aws_sdk_application_signals.types.selection_type.serialize_json(
        value["type"]
    )
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> SelectionConfig:
    out: SelectionConfig = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_application_signals.types.selection_type

        out["type"] = aws_sdk_application_signals.types.selection_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("SelectionConfig.type required")
    if "Pattern" in data:
        out["pattern"] = data["Pattern"]
    return out
