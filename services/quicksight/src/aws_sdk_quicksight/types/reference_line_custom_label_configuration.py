"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineCustomLabelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.non_empty_string


class ReferenceLineCustomLabelConfiguration(TypedDict):
    custom_label: "aws_sdk_quicksight.types.non_empty_string.NonEmptyString"
    """<p>The string text of the custom label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineCustomLabelConfiguration) -> dict:
    out: dict = {}
    out["CustomLabel"] = value["custom_label"]
    return out


def deserialize_json(data: dict) -> ReferenceLineCustomLabelConfiguration:
    out: ReferenceLineCustomLabelConfiguration = {}  # type: ignore[typeddict-item]
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    else:
        raise DeserializationError(
            "ReferenceLineCustomLabelConfiguration.custom_label required"
        )
    return out
