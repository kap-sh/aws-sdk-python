"""Generated from Smithy shape ``com.amazonaws.controltower#EnableBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.baseline_version
    import aws_sdk_controltower.types.enabled_baseline_parameters
    import aws_sdk_controltower.types.tag_map


class EnableBaselineInput(TypedDict, closed=True):
    baseline_version: "aws_sdk_controltower.types.baseline_version.BaselineVersion"
    """<p>The specific version to be enabled of the specified baseline.</p>"""
    parameters: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
    ]
    """<p>A list of <code>key-value</code> objects that specify enablement parameters, where <code>key</code> is a string and <code>value</code> is a document of any type.</p>"""
    baseline_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p>The ARN of the baseline to be enabled.</p>"""
    target_identifier: "aws_sdk_controltower.types.arn.Arn"
    """<p>The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.</p>"""
    tags: NotRequired["aws_sdk_controltower.types.tag_map.TagMap"]
    """<p>Tags associated with input to <code>EnableBaseline</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableBaselineInput) -> dict:
    out: dict = {}
    out["baselineVersion"] = value["baseline_version"]
    if "parameters" in value:
        import aws_sdk_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            aws_sdk_controltower.types.enabled_baseline_parameters.serialize_json(
                value["parameters"]
            )
        )
    out["baselineIdentifier"] = value["baseline_identifier"]
    out["targetIdentifier"] = value["target_identifier"]
    if "tags" in value:
        import aws_sdk_controltower.types.tag_map

        out["tags"] = aws_sdk_controltower.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EnableBaselineInput:
    out: EnableBaselineInput = {}  # type: ignore[typeddict-item]
    if "baselineVersion" in data:
        out["baseline_version"] = data["baselineVersion"]
    else:
        raise DeserializationError("EnableBaselineInput.baseline_version required")
    if "parameters" in data:
        import aws_sdk_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            aws_sdk_controltower.types.enabled_baseline_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if "baselineIdentifier" in data:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        raise DeserializationError("EnableBaselineInput.baseline_identifier required")
    if "targetIdentifier" in data:
        out["target_identifier"] = data["targetIdentifier"]
    else:
        raise DeserializationError("EnableBaselineInput.target_identifier required")
    if "tags" in data:
        import aws_sdk_controltower.types.tag_map

        out["tags"] = aws_sdk_controltower.types.tag_map.deserialize_json(data["tags"])
    return out
