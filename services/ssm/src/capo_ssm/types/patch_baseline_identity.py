"""Generated from Smithy shape ``com.amazonaws.ssm#PatchBaselineIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_description
    import capo_ssm.types.baseline_id
    import capo_ssm.types.baseline_name
    import capo_ssm.types.default_baseline
    import capo_ssm.types.operating_system


class PatchBaselineIdentity(TypedDict, closed=True):
    baseline_id: NotRequired["capo_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the patch baseline.</p>"""
    baseline_name: NotRequired["capo_ssm.types.baseline_name.BaselineName"]
    """<p>The name of the patch baseline.</p>"""
    operating_system: NotRequired["capo_ssm.types.operating_system.OperatingSystem"]
    """<p>Defines the operating system the patch baseline applies to. The default value is <code>WINDOWS</code>. </p>"""
    baseline_description: NotRequired[
        "capo_ssm.types.baseline_description.BaselineDescription"
    ]
    """<p>The description of the patch baseline.</p>"""
    default_baseline: "capo_ssm.types.default_baseline.DefaultBaseline"
    """<p>Indicates whether this is the default baseline. Amazon Web Services Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchBaselineIdentity) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "baseline_name" in value:
        out["BaselineName"] = value["baseline_name"]
    if "operating_system" in value:
        import capo_ssm.types.operating_system

        out["OperatingSystem"] = capo_ssm.types.operating_system.serialize_aws_json_1_1(
            value["operating_system"]
        )
    if "baseline_description" in value:
        out["BaselineDescription"] = value["baseline_description"]
    out["DefaultBaseline"] = value.get("default_baseline", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchBaselineIdentity:
    out: PatchBaselineIdentity = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    if "BaselineName" in data:
        out["baseline_name"] = data["BaselineName"]
    if "OperatingSystem" in data:
        import capo_ssm.types.operating_system

        out["operating_system"] = (
            capo_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if "BaselineDescription" in data:
        out["baseline_description"] = data["BaselineDescription"]
    if "DefaultBaseline" in data:
        out["default_baseline"] = data["DefaultBaseline"]
    else:
        out["default_baseline"] = False
    return out
