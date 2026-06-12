"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateVocabularyFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.data_access_role_arn
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.tag_list
    import aws_sdk_transcribe.types.uri
    import aws_sdk_transcribe.types.vocabulary_filter_name
    import aws_sdk_transcribe.types.words


class CreateVocabularyFilterRequest(TypedDict):
    vocabulary_filter_name: (
        "aws_sdk_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    )
    """<p>A unique name, chosen by you, for your new custom vocabulary filter.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom vocabulary filter with the same name as an existing custom vocabulary filter, you get a <code>ConflictException</code> error.</p>"""
    language_code: "aws_sdk_transcribe.types.language_code.LanguageCode"
    """<p>The language code that represents the language of the entries in your vocabulary filter. Each custom vocabulary filter must contain terms in only one language.</p> <p>A custom vocabulary filter can only be used to transcribe files in the same language as the filter. For example, if you create a custom vocabulary filter using US English (<code>en-US</code>), you can only apply this filter to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html\">Supported languages</a> table.</p>"""
    words: NotRequired["aws_sdk_transcribe.types.words.Words"]
    """<p>Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for creating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFilterFileUri</code> parameter.</p> <p>Note that if you include <code>Words</code> in your request, you cannot use <code>VocabularyFilterFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html\">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>"""
    vocabulary_filter_file_uri: NotRequired["aws_sdk_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt</code> </p> <p>Note that if you include <code>VocabularyFilterFileUri</code> in your request, you cannot use <code>Words</code>; you must choose one or the other.</p>"""
    tags: NotRequired["aws_sdk_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom vocabulary filter at the time you create this new vocabulary filter.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html\">Tagging resources</a>.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns\">IAM ARNs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVocabularyFilterRequest) -> dict:
    out: dict = {}
    import aws_sdk_transcribe.types.language_code

    out["LanguageCode"] = aws_sdk_transcribe.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "words" in value:
        import aws_sdk_transcribe.types.words

        out["Words"] = aws_sdk_transcribe.types.words.serialize_aws_json_1_1(
            value["words"]
        )
    if "vocabulary_filter_file_uri" in value:
        out["VocabularyFilterFileUri"] = value["vocabulary_filter_file_uri"]
    if "tags" in value:
        import aws_sdk_transcribe.types.tag_list

        out["Tags"] = aws_sdk_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVocabularyFilterRequest:
    out: CreateVocabularyFilterRequest = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVocabularyFilterRequest.language_code required"
        )
    if "Words" in data:
        import aws_sdk_transcribe.types.words

        out["words"] = aws_sdk_transcribe.types.words.deserialize_aws_json_1_1(
            data["Words"]
        )
    if "VocabularyFilterFileUri" in data:
        out["vocabulary_filter_file_uri"] = data["VocabularyFilterFileUri"]
    if "Tags" in data:
        import aws_sdk_transcribe.types.tag_list

        out["tags"] = aws_sdk_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    return out
