"""Generated from Smithy shape ``com.amazonaws.connect#ListDefaultVocabulariesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result100
    import aws_sdk_connect.types.vocabulary_language_code
    import aws_sdk_connect.types.vocabulary_next_token


class ListDefaultVocabulariesRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    language_code: NotRequired[
        "aws_sdk_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    ]
    """<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\">What is Amazon Transcribe?</a> </p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired[
        "aws_sdk_connect.types.vocabulary_next_token.VocabularyNextToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDefaultVocabulariesRequest) -> dict:
    out: dict = {}
    if "language_code" in value:
        import aws_sdk_connect.types.vocabulary_language_code

        out["LanguageCode"] = (
            aws_sdk_connect.types.vocabulary_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDefaultVocabulariesRequest:
    out: ListDefaultVocabulariesRequest = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_connect.types.vocabulary_language_code

        out["language_code"] = (
            aws_sdk_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
