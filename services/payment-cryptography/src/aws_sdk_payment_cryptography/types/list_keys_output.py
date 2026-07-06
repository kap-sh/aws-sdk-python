"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListKeysOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_summary_list
    import aws_sdk_payment_cryptography.types.next_token


class ListKeysOutput(TypedDict, closed=True):
    keys: "aws_sdk_payment_cryptography.types.key_summary_list.KeySummaryList"
    """<p>The list of keys created within the caller's Amazon Web Services account and Amazon Web Services Region.</p>"""
    next_token: NotRequired["aws_sdk_payment_cryptography.types.next_token.NextToken"]
    """<p>The token for the next set of results, or an empty or null value if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListKeysOutput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.key_summary_list

    out["Keys"] = (
        aws_sdk_payment_cryptography.types.key_summary_list.serialize_aws_json_1_0(
            value["keys"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListKeysOutput:
    out: ListKeysOutput = {}  # type: ignore[typeddict-item]
    if "Keys" in data:
        import aws_sdk_payment_cryptography.types.key_summary_list

        out["keys"] = (
            aws_sdk_payment_cryptography.types.key_summary_list.deserialize_aws_json_1_0(
                data["Keys"]
            )
        )
    else:
        raise DeserializationError("ListKeysOutput.keys required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
