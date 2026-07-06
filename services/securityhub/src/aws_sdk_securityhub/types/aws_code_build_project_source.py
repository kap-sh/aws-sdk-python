"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectSource(TypedDict, closed=True):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of repository that contains the source code to be built. Valid values are:</p> <ul> <li> <p> <code>BITBUCKET</code> - The source code is in a Bitbucket repository.</p> </li> <li> <p> <code>CODECOMMIT</code> - The source code is in an CodeCommit repository.</p> </li> <li> <p> <code>CODEPIPELINE</code> - The source code settings are specified in the source action of a pipeline in CodePipeline.</p> </li> <li> <p> <code>GITHUB</code> - The source code is in a GitHub repository.</p> </li> <li> <p> <code>GITHUB_ENTERPRISE</code> - The source code is in a GitHub Enterprise repository.</p> </li> <li> <p> <code>NO_SOURCE</code> - The project does not have input source code.</p> </li> <li> <p> <code>S3</code> - The source code is in an S3 input bucket. </p> </li> </ul>"""
    location: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Information about the location of the source code to be built.</p> <p>Valid values include:</p> <ul> <li> <p>For source code settings that are specified in the source action of a pipeline in CodePipeline, location should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipeline's source action instead of this value.</p> </li> <li> <p>For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec file (for example, <code>https://git-codecommit.region-ID.amazonaws.com/v1/repos/repo-name</code> ).</p> </li> <li> <p>For source code in an S3 input bucket, one of the following.</p> <ul> <li> <p>The path to the ZIP file that contains the source code (for example, <code>bucket-name/path/to/object-name.zip</code>).</p> </li> <li> <p> The path to the folder that contains the source code (for example, <code>bucket-name/path/to/source-code/folder/</code>).</p> </li> </ul> </li> <li> <p>For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec file.</p> </li> <li> <p>For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec file. </p> </li> </ul>"""
    git_clone_depth: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Information about the Git clone depth for the build project.</p>"""
    insecure_ssl: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to ignore SSL warnings while connecting to the project source code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectSource) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "location" in value:
        out["Location"] = value["location"]
    if "git_clone_depth" in value:
        out["GitCloneDepth"] = value["git_clone_depth"]
    if "insecure_ssl" in value:
        out["InsecureSsl"] = value["insecure_ssl"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectSource:
    out: AwsCodeBuildProjectSource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "GitCloneDepth" in data:
        out["git_clone_depth"] = data["GitCloneDepth"]
    if "InsecureSsl" in data:
        out["insecure_ssl"] = data["InsecureSsl"]
    return out
