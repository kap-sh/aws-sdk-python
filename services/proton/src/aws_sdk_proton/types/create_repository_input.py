"""Generated from Smithy shape ``com.amazonaws.proton#CreateRepositoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.tag_list


class CreateRepositoryInput(TypedDict):
    provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name (for example, <code>myrepos/myrepo</code>).</p>"""
    connection_arn: "aws_sdk_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html\">Setting up for Proton</a> in the <i>Proton User Guide</i>.</p>"""
    encryption_key: NotRequired["aws_sdk_proton.types.arn.Arn"]
    """<p>The ARN of your customer Amazon Web Services Key Management Service (Amazon Web Services KMS) key.</p>"""
    tags: NotRequired["aws_sdk_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton repository. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRepositoryInput) -> dict:
    out: dict = {}
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    out["connectionArn"] = value["connection_arn"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "tags" in value:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRepositoryInput:
    out: CreateRepositoryInput = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("CreateRepositoryInput.provider required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRepositoryInput.name required")
    if "connectionArn" in data:
        out["connection_arn"] = data["connectionArn"]
    else:
        raise DeserializationError("CreateRepositoryInput.connection_arn required")
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "tags" in data:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
