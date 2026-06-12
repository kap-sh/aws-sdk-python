"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeCodeCoveragesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.code_coverages
    import aws_sdk_codebuild.types.string


class DescribeCodeCoveragesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to <code>DescribeCodeCoverages</code> to retrieve the next set of items.</p>"""
    code_coverages: NotRequired["aws_sdk_codebuild.types.code_coverages.CodeCoverages"]
    """<p>An array of <code>CodeCoverage</code> objects that contain the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCodeCoveragesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "code_coverages" in value:
        import aws_sdk_codebuild.types.code_coverages

        out["codeCoverages"] = (
            aws_sdk_codebuild.types.code_coverages.serialize_aws_json_1_1(
                value["code_coverages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCodeCoveragesOutput:
    out: DescribeCodeCoveragesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "codeCoverages" in data:
        import aws_sdk_codebuild.types.code_coverages

        out["code_coverages"] = (
            aws_sdk_codebuild.types.code_coverages.deserialize_aws_json_1_1(
                data["codeCoverages"]
            )
        )
    return out
