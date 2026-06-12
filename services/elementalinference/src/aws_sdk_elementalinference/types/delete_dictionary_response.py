"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteDictionaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_arn
    import aws_sdk_elementalinference.types.dictionary_id
    import aws_sdk_elementalinference.types.dictionary_status


class DeleteDictionaryResponse(TypedDict):
    arn: "aws_sdk_elementalinference.types.dictionary_arn.DictionaryArn"
    """<p>The ARN of the deleted dictionary.</p>"""
    id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the deleted dictionary.</p>"""
    status: "aws_sdk_elementalinference.types.dictionary_status.DictionaryStatus"
    """<p>The status of the dictionary after deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDictionaryResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import aws_sdk_elementalinference.types.dictionary_status

    out["status"] = aws_sdk_elementalinference.types.dictionary_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDictionaryResponse:
    out: DeleteDictionaryResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteDictionaryResponse.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteDictionaryResponse.id required")
    if "status" in data:
        import aws_sdk_elementalinference.types.dictionary_status

        out["status"] = (
            aws_sdk_elementalinference.types.dictionary_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteDictionaryResponse.status required")
    return out
