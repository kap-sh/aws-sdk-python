"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListDictionariesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_summary_list


class ListDictionariesResponse(TypedDict):
    dictionaries: (
        "aws_sdk_elementalinference.types.dictionary_summary_list.DictionarySummaryList"
    )
    """<p>A list of DictionarySummary objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDictionariesResponse) -> dict:
    out: dict = {}
    import aws_sdk_elementalinference.types.dictionary_summary_list

    out["dictionaries"] = (
        aws_sdk_elementalinference.types.dictionary_summary_list.serialize_json(
            value["dictionaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDictionariesResponse:
    out: ListDictionariesResponse = {}  # type: ignore[typeddict-item]
    if "dictionaries" in data:
        import aws_sdk_elementalinference.types.dictionary_summary_list

        out["dictionaries"] = (
            aws_sdk_elementalinference.types.dictionary_summary_list.deserialize_json(
                data["dictionaries"]
            )
        )
    else:
        raise DeserializationError("ListDictionariesResponse.dictionaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
