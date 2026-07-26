"""Generated from Smithy shape ``com.amazonaws.ssm#PutParameterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter_tier
    import capo_ssm.types.ps_parameter_version


class PutParameterResult(TypedDict, closed=True):
    version: "capo_ssm.types.ps_parameter_version.PSParameterVersion"
    """<p>The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter version ID in API operations or in Systems Manager documents (SSM documents). By default, if you don't specify a specific version, the system returns the latest parameter value when a parameter is called.</p>"""
    tier: NotRequired["capo_ssm.types.parameter_tier.ParameterTier"]
    """<p>The tier assigned to the parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutParameterResult) -> dict:
    out: dict = {}
    out["Version"] = value.get("version", 0)
    if "tier" in value:
        import capo_ssm.types.parameter_tier

        out["Tier"] = capo_ssm.types.parameter_tier.serialize_aws_json_1_1(
            value["tier"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutParameterResult:
    out: PutParameterResult = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "Tier" in data:
        import capo_ssm.types.parameter_tier

        out["tier"] = capo_ssm.types.parameter_tier.deserialize_aws_json_1_1(
            data["Tier"]
        )
    return out
