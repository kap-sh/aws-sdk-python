"""Generated from Smithy shape ``com.amazonaws.sns#ListOriginationNumbersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.next_token
    import aws_sdk_sns.types.phone_number_information_list


class ListOriginationNumbersResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sns.types.next_token.nextToken"]
    """<p>A <code>NextToken</code> string is returned when you call the <code>ListOriginationNumbers</code> operation if additional pages of records are available.</p>"""
    phone_numbers: NotRequired[
        "aws_sdk_sns.types.phone_number_information_list.PhoneNumberInformationList"
    ]
    """<p>A list of the calling account's verified and pending origination numbers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOriginationNumbersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "phone_numbers" in value:
        import aws_sdk_sns.types.phone_number_information_list

        aws_sdk_sns.types.phone_number_information_list.serialize_query(
            value["phone_numbers"], pairs, f"{prefix}.PhoneNumbers"
        )


def deserialize_query(el: Element) -> ListOriginationNumbersResult:
    out: ListOriginationNumbersResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_phone_numbers = el.find("PhoneNumbers")
    if child_phone_numbers is not None:
        import aws_sdk_sns.types.phone_number_information_list

        out["phone_numbers"] = (
            aws_sdk_sns.types.phone_number_information_list.deserialize_query(
                child_phone_numbers
            )
        )
    return out
