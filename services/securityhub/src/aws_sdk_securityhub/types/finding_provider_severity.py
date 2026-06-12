"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingProviderSeverity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.severity_label


class FindingProviderSeverity(TypedDict):
    label: NotRequired["aws_sdk_securityhub.types.severity_label.SeverityLabel"]
    """<p>The severity label assigned to the finding by the finding provider.</p>"""
    original: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The finding provider's original value for the severity.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 64.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingProviderSeverity) -> dict:
    out: dict = {}
    if "label" in value:
        import aws_sdk_securityhub.types.severity_label

        out["Label"] = aws_sdk_securityhub.types.severity_label.serialize_json(
            value["label"]
        )
    if "original" in value:
        out["Original"] = value["original"]
    return out


def deserialize_json(data: dict) -> FindingProviderSeverity:
    out: FindingProviderSeverity = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        import aws_sdk_securityhub.types.severity_label

        out["label"] = aws_sdk_securityhub.types.severity_label.deserialize_json(
            data["Label"]
        )
    if "Original" in data:
        out["original"] = data["Original"]
    return out
