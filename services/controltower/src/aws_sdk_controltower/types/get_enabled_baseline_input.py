"""Generated from Smithy shape ``com.amazonaws.controltower#GetEnabledBaselineInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn


class GetEnabledBaselineInput(TypedDict):
    enabled_baseline_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p>Identifier of the <code>EnabledBaseline</code> resource to be retrieved, in ARN format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledBaselineInput) -> dict:
    out: dict = {}
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> GetEnabledBaselineInput:
    out: GetEnabledBaselineInput = {}  # type: ignore[typeddict-item]
    if "enabledBaselineIdentifier" in data:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        raise DeserializationError(
            "GetEnabledBaselineInput.enabled_baseline_identifier required"
        )
    return out
