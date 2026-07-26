"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.next_token
    import capo_payment_cryptography.types.tags


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "capo_payment_cryptography.types.tags.Tags"
    """<p>The list of tags associated with a <code>ResourceArn</code>. Each tag will list the key-value pair contained within that tag.</p>"""
    next_token: NotRequired["capo_payment_cryptography.types.next_token.NextToken"]
    """<p>The token for the next set of results, or an empty or null value if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.tags

    out["Tags"] = capo_payment_cryptography.types.tags.serialize_aws_json_1_0(
        value["tags"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_payment_cryptography.types.tags

        out["tags"] = capo_payment_cryptography.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
