"""Generated from Smithy shape ``com.amazonaws.codecommit#GetPullRequestOverrideStateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.overridden


class GetPullRequestOverrideStateOutput(TypedDict):
    overridden: "aws_sdk_codecommit.types.overridden.Overridden"
    """<p>A Boolean value that indicates whether a pull request has had its rules set aside (TRUE) or whether all approval rules still apply (FALSE).</p>"""
    overrider: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPullRequestOverrideStateOutput) -> dict:
    out: dict = {}
    out["overridden"] = value.get("overridden", False)
    if "overrider" in value:
        out["overrider"] = value["overrider"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPullRequestOverrideStateOutput:
    out: GetPullRequestOverrideStateOutput = {}  # type: ignore[typeddict-item]
    if "overridden" in data:
        out["overridden"] = data["overridden"]
    else:
        out["overridden"] = False
    if "overrider" in data:
        out["overrider"] = data["overrider"]
    return out
