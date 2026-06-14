"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateVocabularyFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.data_access_role_arn
    import aws_sdk_transcribe.types.uri
    import aws_sdk_transcribe.types.vocabulary_filter_name
    import aws_sdk_transcribe.types.words


class UpdateVocabularyFilterRequest(TypedDict):
    vocabulary_filter_name: (
        "aws_sdk_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    )
    """<p>The name of the custom vocabulary filter you want to update. Custom vocabulary filter names are case sensitive.</p>"""
    words: NotRequired["aws_sdk_transcribe.types.words.Words"]
    r"""<p>Use this parameter if you want to update your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for updating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFilterFileUri</code> parameter.</p> <p>Note that if you include <code>Words</code> in your request, you cannot use <code>VocabularyFilterFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html\">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>"""
    vocabulary_filter_file_uri: NotRequired["aws_sdk_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt</code> </p> <p>Note that if you include <code>VocabularyFilterFileUri</code> in your request, you cannot use <code>Words</code>; you must choose one or the other.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns\">IAM ARNs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVocabularyFilterRequest) -> dict:
    out: dict = {}
    if "words" in value:
        import aws_sdk_transcribe.types.words

        out["Words"] = aws_sdk_transcribe.types.words.serialize_aws_json_1_1(
            value["words"]
        )
    if "vocabulary_filter_file_uri" in value:
        out["VocabularyFilterFileUri"] = value["vocabulary_filter_file_uri"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVocabularyFilterRequest:
    out: UpdateVocabularyFilterRequest = {}  # type: ignore[typeddict-item]
    if "Words" in data:
        import aws_sdk_transcribe.types.words

        out["words"] = aws_sdk_transcribe.types.words.deserialize_aws_json_1_1(
            data["Words"]
        )
    if "VocabularyFilterFileUri" in data:
        out["vocabulary_filter_file_uri"] = data["VocabularyFilterFileUri"]
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    return out
