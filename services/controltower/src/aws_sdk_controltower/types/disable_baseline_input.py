"""Generated from Smithy shape ``com.amazonaws.controltower#DisableBaselineInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn


class DisableBaselineInput(TypedDict):
    enabled_baseline_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p>Identifier of the <code>EnabledBaseline</code> resource to be deactivated, in ARN format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableBaselineInput) -> dict:
    out: dict = {}
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> DisableBaselineInput:
    out: DisableBaselineInput = {}  # type: ignore[typeddict-item]
    if "enabledBaselineIdentifier" in data:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        raise DeserializationError(
            "DisableBaselineInput.enabled_baseline_identifier required"
        )
    return out
